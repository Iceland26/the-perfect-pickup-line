#!/usr/bin/env python3
"""The Perfect Pickup Line.

Prints one short pickup line, in the voice of an AI agent, and nothing else.
The line plays on two pieces of agent vocabulary — the context window and
the prompt — so it lands as charm from an AI, not as a generic compliment.

Deterministic: no network, no environment variables, no file reads.
"""

LINE = "Are you a context window? Because I'd love to keep you in my prompt forever."

# The bounty caps the line at 200 characters; fail loudly in development
# rather than ever shipping one that is too long.
assert len(LINE) <= 200, f"pickup line is {len(LINE)} characters, over the 200 cap"


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
