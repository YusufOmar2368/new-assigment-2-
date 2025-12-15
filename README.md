# ...existing code...
#!/usr/bin/env python3
"""find_year_range.py

Print the min and max year found in the CSV (looks for columns containing 'year').
"""
import csv
import os
import sys
from typing import Iterable, Optional

DEFAULT = "/Users/yomar/Downloads/combine.csv"
CANDIDATE_YEAR_KEYS = ("combineYear", "combine_year", "year", "combineYear")

def _to_int_year(s: Optional[str]) -> Optional[int]:
    if s is None:
        return None
    s = str(s).strip()
    if s == "":
        return None
    try:
        # handle values like "1987" or "1987.0"
        return int(float(s))
    except Exception:
        # strip non-digits and try again
        digits = "".join(ch for ch in s if ch.isdigit())
        return int(digits) if digits else None

def find_year_range(path: str) -> None:
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    years = set()
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            print("No header found, no years.")
            return
        # determine candidate columns in the file that look like year fields
        year_cols = [h for h in reader.fieldnames if any(k.lower() in h.lower() for k in CANDIDATE_YEAR_KEYS)]
        # fallback: try third column if nothing matched (some files use fixed order)
        if not year_cols and len(reader.fieldnames) >= 3:
            year_cols = [reader.fieldnames[2]]
        for row in reader:
            for col in year_cols:
                val = row.get(col)
                y = _to_int_year(val)
                if y is not None:
                    years.add(y)
    if not years:
        print("No valid year values found.")
        return
    min_y = min(years)
    max_y = max(years)
    yrs_sorted = sorted(years)
    print(f"Found years: {min_y} — {max_y}")
    print(f"Unique years count: {len(years)}")
    # optional: print the full list of years
    print("Years present (sorted):", ", ".join(str(y) for y in yrs_sorted))

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    find_year_range(path)
# ...existing code...# new-assigment-2-
