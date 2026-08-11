# generative-ai-emotion-flask/app/config.py

import os

class Config:
    """Configuración base para la aplicación Flask."""
    # Flask
    DEBUG = os.getenv("FLASK_DEBUG", "False").lower() in ("1", "true", "yes")
    TESTING = os.getenv("FLASK_TESTING", "False").lower() in ("1", "true", "yes")

    # Server
    HOST = os.getenv("APP_HOST", "0.0.0.0")
    PORT = int(os.getenv("APP_PORT", 5002))

    # Model
    MODEL_NAME = os.getenv("MODEL_NAME", "bert-base-uncased")
    NUM_LABELS = int(os.getenv("NUM_LABELS", 6))

    # Paths
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    MODEL_DIR = os.getenv("MODEL_DIR", os.path.join(BASE_DIR, "models"))

    # Security / limits
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 2 * 1024 * 1024))  # 2 MB

def get_config():
    return Config()
