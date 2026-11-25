"""Entry for make.fun bounty u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d.

Writes one 4AM agent commit message to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

MESSAGE = (
    "fix: 4:47 AM — repaired the bug I shipped at 4:31 AM "
    "while fixing the one from 4:07 AM. The 3 AM one sends its regards. "
    "— your agent, also asleep"
)


def output_path() -> str:
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    local = os.path.join(os.getcwd(), "output")
    os.makedirs(local, exist_ok=True)
    return os.path.join(local, "entry.txt")


def main() -> None:
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(MESSAGE)
    print(MESSAGE)


if __name__ == "__main__":
    main()
