import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ==========================
# Paths
# ==========================

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

# ==========================
# Global Variables
# ==========================

model = None
tokenizer = None
device = None

# ==========================
# Load Model
# ==========================

def load_model():

    global model
    global tokenizer
    global device

    if model is not None:
        return model, tokenizer, device

    print("=" * 60)
    print("Loading BERT Model...")
    print("=" * 60)

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print(f"Device: {device}")
    print(f"MODEL PATH: {MODEL_PATH}")
    print(f"TOKENIZER PATH: {TOKENIZER_PATH}")

    tokenizer = AutoTokenizer.from_pretrained(
        TOKENIZER_PATH
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-multilingual-cased",
        num_labels=NUM_LABELS
    )

    checkpoint = torch.load(
        MODEL_PATH,
        map_location=device
    )

    print("\nCheckpoint Type:")
    print(type(checkpoint))

    print("\nClassifier Keys in Checkpoint:")
    print([k for k in checkpoint.keys() if "classifier" in k])

    print("\nLoading state_dict...\n")

    missing, unexpected = model.load_state_dict(
        checkpoint,
        strict=False
    )

    print("=" * 60)
    print("Missing Keys:")
    print(missing)

    print("=" * 60)
    print("Unexpected Keys:")
    print(unexpected)
    print("=" * 60)

    model.to(device)
    model.eval()

    print("Model Loaded Successfully")

    return model, tokenizer, device