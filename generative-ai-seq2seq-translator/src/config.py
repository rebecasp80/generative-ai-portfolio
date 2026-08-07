import torch
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

EMBED_DIM = 256
HIDDEN_DIM = 512
NUM_LAYERS = 1
DROPOUT = 0.1

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
