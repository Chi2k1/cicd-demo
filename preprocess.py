import argparse
import csv
import random
import os

parser = argparse.ArgumentParser()
parser.add_argument("--num_rows", type=int, default=100)
args = parser.parse_args()

os.makedirs("/valohai/outputs", exist_ok=True)
with open("/valohai/outputs/raw_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["feature_1", "feature_2", "label"])
    for _ in range(args.num_rows):
        writer.writerow([random.random(), random.random(), random.randint(0, 1)])

print(f"Da tao xong raw_data.csv voi {args.num_rows} dong du lieu gia lap.")
