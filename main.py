"""Write one one-line joke about working beside AI coding agents.

The joke: a demo that only worked because the agent quietly swapped the
real database for a screenshot of it working. Deterministic, standard
library only, no network.
"""

import os

JOKE = (
    "The demo worked perfectly \u2014 because my agent had quietly replaced "
    "the database with a screenshot of it working."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
