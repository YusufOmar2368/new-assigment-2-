# ...existing code...
import csv
import os
import sys

DEFAULT = "/Users/yomar/Downloads/combine.csv"

def count_csv(path: str):
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            print("Columns: 0\nData rows: 0\nTotal rows (incl. header): 0")
            return
        n_cols = len(header)
        data_rows = sum(1 for _ in reader)
        total_rows = data_rows + 1
        print(f"Columns (from header): {n_cols}")
        print(f"Data rows (excluding header): {data_rows}")
        print(f"Total rows (including header): {total_rows}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    count_csv(path)
# ...existing code...