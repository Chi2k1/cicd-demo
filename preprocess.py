import csv
import random
import os

os.makedirs("/valohai/outputs", exist_ok=True)
with open("/valohai/outputs/raw_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["feature_1", "feature_2", "label"])
    for _ in range(100):
        writer.writerow([random.random(), random.random(), random.randint(0, 1)])

print("Da tao xong raw_data.csv voi 100 dong du lieu gia lap.")
