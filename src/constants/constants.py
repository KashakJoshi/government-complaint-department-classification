from pathlib import Path


# ==========================
# Project Root
# ==========================

PROJECT_ROOT = Path(__file__).resolve().parents[2]


# ==========================
# Configuration Files
# ==========================

CONFIG_DIR = PROJECT_ROOT / "configs"

CONFIG_FILE = CONFIG_DIR / "config.yaml"
MODEL_CONFIG_FILE = CONFIG_DIR / "model.yaml"
PARAMS_FILE = CONFIG_DIR / "params.yaml"
PATHS_FILE = CONFIG_DIR / "paths.yaml"


# ==========================
# File Encodings
# ==========================

UTF8 = "utf-8"


# ==========================
# Supported Input Types
# ==========================

TEXT = "text"
IMAGE = "image"
AUDIO = "audio"


# ==========================
# Supported Image Extensions
# ==========================

SUPPORTED_IMAGE_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tiff",
)


# ==========================
# Supported Audio Extensions
# ==========================

SUPPORTED_AUDIO_EXTENSIONS = (
    ".wav",
    ".mp3",
    ".m4a",
    ".ogg",
)


# ==========================
# Supported Text Extensions
# ==========================

SUPPORTED_TEXT_EXTENSIONS = (
    ".txt",
)