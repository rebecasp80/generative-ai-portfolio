import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class ModelLoader:
    def __init__(self, model_name="llama-3.1-8b-instant"):
        print(">>> MODEL_LOADER CARGADO <<<")
        print(f"[ModelLoader] Initializing Groq client with model: {model_name}")

        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")

        self.client = Groq(api_key=api_key)
        self.model_name = model_name

        print("[ModelLoader] Groq client initialized successfully.")

    def get_client(self):
        return self.client

    def get_model_name(self):
        return self.model_name
