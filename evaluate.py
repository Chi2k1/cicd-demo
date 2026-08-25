import json
import pickle
import glob
import os

model_path = glob.glob("/valohai/inputs/model_file/*.pkl")[0]
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Danh gia gia lap
accuracy = 0.87

result = {"accuracy": accuracy, "threshold_used": model["threshold"]}

os.makedirs("/valohai/outputs", exist_ok=True)
with open("/valohai/outputs/evaluation.json", "w") as f:
    json.dump(result, f)

print(json.dumps(result))
