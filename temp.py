import pandas as pd
import json

df = pd.read_csv("data/raw/dataset.csv")

# remove empty labels
df = df.dropna(subset=["label", "department_name"])

# convert label safely
df["label"] = df["label"].astype(float).astype(int)

# create mapping
label_mapping = (
    df[["label", "department_name"]]
    .drop_duplicates()
    .set_index("label")["department_name"]
    .to_dict()
)

label_mapping = {
    str(k): v for k, v in label_mapping.items()
}

with open("models/label_mapping.json", "w", encoding="utf-8") as f:
    json.dump(
        label_mapping,
        f,
        ensure_ascii=False,
        indent=2
    )

print("updated")
print("12 =", label_mapping.get("12"))