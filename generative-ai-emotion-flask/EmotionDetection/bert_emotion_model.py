from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
)
from peft import PeftModel
import torch
import os


class EmotionModel:
    """
    Clase principal para detección de emociones con soporte para modelos base,
    LoRA, QLoRA y Adapters.
    """

    def __init__(self, model_type: str = "base", model_path: str = None):
        """
        Inicializa el modelo según el tipo especificado.
        :param model_type: 'base', 'lora', 'qlora' o 'adapter'
        :param model_path: ruta al modelo fine-tuneado (si aplica)
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_type = model_type.lower()
        self.model_path = model_path or f"models/{self.model_type}/"

        # Tokenizador base
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

        # Cargar modelo según tipo
        if self.model_type == "base":
            self.model = AutoModelForSequenceClassification.from_pretrained(
                "bert-base-uncased", num_labels=6
            )
        else:
            # Cargar modelo base y aplicar PEFT (LoRA, QLoRA o Adapter)
            base_model = AutoModelForSequenceClassification.from_pretrained(
                "bert-base-uncased", num_labels=6
            )
            self.model = PeftModel.from_pretrained(base_model, self.model_path)

        self.model.to(self.device)
        self.model.eval()

    def predict(self, text: str):
        """
        Realiza la predicción de emoción para un texto dado.
        :param text: texto de entrada
        :return: etiqueta dominante y probabilidades
        """
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128,
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

        label = torch.argmax(probs).item()
        return label, probs.cpu().tolist()

    def available_models(self):
        """
        Devuelve los modelos disponibles en la carpeta 'models/'.
        """
        models_dir = "models/"
        if not os.path.exists(models_dir):
            return []
        return [d for d in os.listdir(models_dir) if os.path.isdir(os.path.join(models_dir, d))]
