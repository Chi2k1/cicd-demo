import csv
import json
import os
import pickle
import glob

input_path = glob.glob("/valohai/inputs/input_data/*.csv")[0]

rows = []
with open(input_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# "Train" gia lap: tinh trung binh feature_1 lam nguong phan loai
avg = sum(float(r["feature_1"]) for r in rows) / len(rows)
model = {"threshold": avg}

os.makedirs("/valohai/outputs", exist_ok=True)
with open("/valohai/outputs/model.pkl", "wb") as f:
    pickle.dump(model, f)

print(json.dumps({"training_samples": len(rows), "threshold": avg}))
