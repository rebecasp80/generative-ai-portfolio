import requests

class ChatbotEngine:
    def __init__(self):
        # 🔑 Tu API Key de Groq
        self.api_key = "MY_API_KEY"

        # 🧠 Modelo base
        self.model_name = "llama-3.1-8b-instant"

        # 💬 Memoria de conversación
        self.conversation_history = []

        # 🎯 Prompt del sistema
        self.system_prompt = {
            "role": "system",
            "content": "Eres un asistente amable, claro y útil."
        }

    def generate_response(self, user_message):
        """Genera una respuesta usando la API REST de Groq."""
        self.conversation_history.append({"role": "user", "content": user_message})

        messages = [self.system_prompt] + self.conversation_history

        # 🔗 Llamada directa a la API de Groq
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": self.model_name,
                "messages": messages,
                "temperature": 0.8,
                "max_tokens": 512,
                "top_p": 0.9
                # ⚠️ Eliminado repetition_penalty (no soportado)
            }
        )

        data = response.json()

        # 🧩 Mostrar respuesta completa en consola para depuración
        print("\n=== RESPUESTA GROQ ===")
        print(data)
        print("======================\n")

        # ⚠️ Si hay error, mostrarlo en la interfaz
        if "error" in data:
            return f"⚠ Error de Groq: {data['error']['message']}"

        # ⚠️ Si no hay respuesta válida
        if "choices" not in data or not data["choices"]:
            return "⚠ Groq no devolvió ninguna respuesta."

        # ✅ Extraer respuesta del modelo
        bot_reply = data["choices"][0]["message"]["content"]

        # Guardar respuesta en memoria
        self.conversation_history.append({"role": "assistant", "content": bot_reply})

        return bot_reply

    def clear_memory(self):
        """Limpia la memoria de conversación."""
        self.conversation_history = []
