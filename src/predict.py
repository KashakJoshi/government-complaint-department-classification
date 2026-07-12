import torch
import torch.nn.functional as F
import json
import os

from src.load_model import load_model

# Load model once
model, tokenizer, device = load_model()


# Load label mapping
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


LABEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "label_mapping.json"
)


with open(
    LABEL_PATH,
    "r",
    encoding="utf-8"
) as f:
    label_mapping = json.load(f)



def predict_department(text):


    inputs = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt"
    )


    input_ids = inputs["input_ids"].to(device)

    attention_mask = inputs["attention_mask"].to(device)



    with torch.no_grad():

        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask
        )


    probabilities = F.softmax(
        outputs.logits,
        dim=1
    )


    confidence, prediction = torch.max(
        probabilities,
        dim=1
    )


    department_id = str(
        prediction.item()
    )


    department_name = label_mapping.get(
        department_id,
        "Unknown"
    )


    return {

        "department_id": int(
            prediction.item()
        ),

        "department_name": department_name,

        "confidence": round(
            float(confidence.item()),
            4
        )
    }



if __name__ == "__main__":

    text = "मेरे गांव की सड़क खराब है"


    result = predict_department(
        text
    )


    print(result)