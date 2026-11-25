#!/usr/bin/env python3
"""Kit guard: checks that look only at lines ADDED by a change (never old code).

Usage:
  guard.py staged        check the staged diff (used by the pre-commit hook)
  guard.py file PATH     check the lines changed in one file since the last commit
                         (used by the Claude Code edit hook)

Checks:
  C  A comment that silences a warning (noqa, type: ignore, eslint-disable ...)
     must give a reason in plain words:   # noqa: BLE001 -- why this is safe
  D  A comment must not excuse a quick fix (workaround, hack, quick fix ...).
  R  If the project has a ruff.toml, ruff runs and only findings on added
     lines count.

Exit code 0 = fine, 1 = problems found (message on stdout, with what to do
instead). Works with the Python 3.9 that ships with macOS.
"""
import json
import os
import re
import shutil
import subprocess
import sys

CODE_EXT = {".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".sh", ".css", ".html"}
SKIP_PREFIXES = (".githooks/",)

SUPPRESS = re.compile(
    r"(noqa|type:\s*ignore|pylint:\s*disable|eslint-disable(?:-next-line|-line)?"
    r"|@ts-ignore|@ts-expect-error|nosec)"
)
REASON = re.compile(r"\s--\s+\S+\s+\S+")  # " -- " then at least two words
EXCUSE = re.compile(
    r"\b(work-?arounds?|hack(?:y|s)?|quick[- ]fix(?:es)?|temporary fix(?:es)?"
    r"|band-?aid|kludges?)\b",
    re.IGNORECASE,
)

RUFF_HINTS = {
    "PGH003": "Name the rule inside the brackets, for example "
              "`# type: ignore[assignment] -- reason`, or fix the type problem.",
    "PGH004": "Name the rule code, for example `# noqa: E402 -- reason`, "
              "or fix the problem instead of silencing it.",
    "RUF100": "Remove the suppression comment: it is not needed.",
}


def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          universal_newlines=True)


def repo_root():
    out = run(["git", "rev-parse", "--show-toplevel"])
    return out.stdout.strip() if out.returncode == 0 else None


def parse_diff(text):
    """Return {path: {line_number: line_text}} for added lines."""
    added = {}
    path = None
    new_line = 0
    for line in text.splitlines():
        if line.startswith("+++ "):
            target = line[4:].strip()
            path = None if target == "/dev/null" else target[2:] if target.startswith("b/") else target
            continue
        if line.startswith("@@"):
            match = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@", line)
            new_line = int(match.group(1)) if match else 0
            continue
        if path is None:
            continue
        if line.startswith("+") and not line.startswith("+++"):
            added.setdefault(path, {})[new_line] = line[1:]
            new_line += 1
        elif line.startswith(" "):
            new_line += 1
    return added


def staged_added_lines():
    out = run(["git", "diff", "--cached", "-U0", "--no-color", "--diff-filter=ACMR"])
    return parse_diff(out.stdout)


def file_added_lines(path):
    root = repo_root()
    if not root:
        return {}
    abs_path = os.path.abspath(path)
    rel = os.path.relpath(abs_path, root)
    if rel.startswith(".."):
        return {}
    tracked = run(["git", "ls-files", "--error-unmatch", rel]).returncode == 0
    has_head = run(["git", "rev-parse", "--verify", "-q", "HEAD"]).returncode == 0
    if tracked and has_head:
        out = run(["git", "diff", "HEAD", "-U0", "--no-color", "--", rel])
        return parse_diff(out.stdout)
    try:
        with open(abs_path, encoding="utf-8", errors="replace") as handle:
            lines = handle.read().splitlines()
    except OSError:
        return {}
    return {rel: {i + 1: text for i, text in enumerate(lines)}}


def comment_text(path, text):
    """Return the comment part of a line, or None when there is none."""
    ext = os.path.splitext(path)[1]
    if ext in (".py", ".sh"):
        index = text.find("#")
        return text[index:] if index >= 0 else None
    if ext in (".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"):
        match = re.search(r"(?<![:\w])//|/\*", text)
        return text[match.start():] if match else None
    if ext == ".css":
        index = text.find("/*")
        return text[index:] if index >= 0 else None
    if ext == ".html":
        index = text.find("<!--")
        return text[index:] if index >= 0 else None
    return None


def check_comments(added):
    problems = []
    for path, lines in sorted(added.items()):
        if os.path.splitext(path)[1] not in CODE_EXT or path.startswith(SKIP_PREFIXES):
            continue
        for number, text in sorted(lines.items()):
            comment = comment_text(path, text)
            if comment is None:
                continue
            suppress = SUPPRESS.search(comment)
            if suppress and not REASON.search(comment[suppress.end():]):
                problems.append(
                    "%s:%d: BLOCKED (guard C): a comment silences a warning but gives no "
                    "reason. Add ' -- <why this is safe, in plain words>' after it, or fix "
                    "the underlying code instead of silencing it." % (path, number)
                )
            excuse = EXCUSE.search(comment)
            if excuse:
                problems.append(
                    "%s:%d: BLOCKED (guard D): the comment says '%s'. Comments must not "
                    "excuse a quick fix. Fix the root cause instead of patching around it. "
                    "If this is a real exception, ask the owner." % (path, number, excuse.group(0))
                )
    return problems


def find_ruff(root):
    for candidate in (os.environ.get("RUFF_BIN"), shutil.which("ruff"),
                      os.path.join(root, ".venv", "bin", "ruff")):
        if candidate and os.path.exists(candidate):
            return candidate
    return None


def check_ruff(added, root, strict):
    config = os.path.join(root, "ruff.toml")
    py_files = [p for p in added if p.endswith(".py") and not p.startswith(SKIP_PREFIXES)]
    if not os.path.exists(config) or not py_files:
        return []
    ruff = find_ruff(root)
    if ruff is None:
        if strict:
            return ["BLOCKED (guard R): this project has a ruff.toml but ruff was not found. "
                    "Install it (pip install ruff) or set RUFF_BIN in .githooks/config.sh."]
        return []
    result = run([ruff, "check", "--config", config, "--no-cache",
                  "--output-format", "json"] + [os.path.join(root, p) for p in py_files])
    try:
        findings = json.loads(result.stdout or "[]")
    except ValueError:
        return ["BLOCKED (guard R): ruff gave output the guard could not read: %s"
                % result.stderr.strip()[:200]]
    problems = []
    for item in findings:
        rel = os.path.relpath(item["filename"], root)
        row = item["location"]["row"]
        if row not in added.get(rel, {}):
            continue
        code = item.get("code") or "ruff"
        hint = RUFF_HINTS.get(code, "Fix the cause rather than silencing the warning.")
        problems.append("%s:%d: BLOCKED (guard R, %s): %s %s"
                        % (rel, row, code, item["message"], hint))
    return problems


def main(argv):
    if len(argv) < 2 or argv[1] not in ("staged", "file"):
        print(__doc__)
        return 2
    root = repo_root()
    if not root:
        return 0
    os.chdir(root)
    if argv[1] == "staged":
        added, strict = staged_added_lines(), True
    else:
        if len(argv) < 3:
            print(__doc__)
            return 2
        added, strict = file_added_lines(argv[2]), False
    problems = check_comments(added) + check_ruff(added, root, strict)
    for problem in problems:
        print(problem)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
