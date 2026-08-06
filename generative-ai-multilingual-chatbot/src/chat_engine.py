from src.model_loader import ModelLoader
from src.tokenizer_utils import TokenizerUtils

class ChatEngine:
    def __init__(self, model_name="llama-3.1-8b-instant"):
        print(">>> CHAT_ENGINE CARGADO <<<")
        print(f">>> MODELO SELECCIONADO: {model_name}")

        self.model_loader = ModelLoader(model_name)
        self.client = self.model_loader.get_client()
        self.model_name = self.model_loader.get_model_name()

        self.tokenizer_utils = TokenizerUtils()

        # 🧠 Memoria conversacional
        self.history = []

        print("[ChatEngine] Chat engine ready.")

    def generate(self, prompt: str, persona="neutral", tone="neutral", lang="es", max_tokens: int = 250):

        tutor_block = ""
        if persona == "tutor":
            tutor_block = """
            Actúa como tutor de idiomas.
            - Corrige errores del usuario.
            - Explica la corrección de forma breve.
            - Da un ejemplo correcto.
            - Mantén frases cortas y claras.
            """

        system_prompt = f"""
        Eres un asistente con personalidad '{persona}'.
        El usuario tiene un tono '{tone}'.
        Responde en el idioma '{lang}'.
        Mantén tus respuestas breves, claras y separadas en frases.
        {tutor_block}
        """

        messages = [{"role": "system", "content": system_prompt}] + self.history + [
            {"role": "user", "content": prompt}
        ]

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.7,
            top_p=0.9
        )

        output = response.choices[0].message.content.strip()

        self.history.append({"role": "assistant", "content": output})

        return output
