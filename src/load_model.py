import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# current file: Complaint_Classifier/src/load_model.py
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_DIR = os.path.dirname(SRC_DIR)


MODEL_PATH = os.path.join(
    PROJECT_DIR,
    "models",
    "best_model.pt"
)

TOKENIZER_PATH = os.path.join(
    PROJECT_DIR,
    "models",
    "tokenizer"
)


NUM_LABELS = 92


device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


def load_model():

    print("MODEL PATH:", MODEL_PATH)
    print("TOKENIZER PATH:", TOKENIZER_PATH)


    tokenizer = AutoTokenizer.from_pretrained(
        "bert-base-multilingual-cased"
    )


    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-multilingual-cased",
        num_labels=NUM_LABELS
    )


    checkpoint = torch.load(
        MODEL_PATH,
        map_location=device
    )


    model.load_state_dict(checkpoint)

    model.to(device)
    model.eval()

    print("Model loaded successfully")

    return model, tokenizer, device