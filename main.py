"""Deadpan forecast for the invented city of Glintwick.

Writes a single weather-forecast line (at most 160 characters) to
/output/entry.txt, as required by the make.fun competition
"Deadpan Forecasts for Cities That Do Not Exist".
"""

import os

ENTRY = (
    "In Glintwick, a light drizzle of confetti is expected by noon, "
    "highs of 19 degrees, and the mayor's umbrella ban enters its "
    "third week."
)


def main() -> None:
    # The line is fixed: the forecast is the deliverable, not a
    # generated variation, so every run writes the same entry.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
