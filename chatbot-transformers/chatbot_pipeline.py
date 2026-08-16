import os
import json
import difflib
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# 🧠 Rutas
BASE_MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "training", "sft_model_neo"))
SFT_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "sft_data.jsonl"))

print(f"🤖 Cargando modelo SFT GPT‑Neo desde:\n{BASE_MODEL_PATH}\n")

# Modelo (no lo usamos para responder, pero lo dejamos cargado por si lo necesitas)
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_PATH, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(BASE_MODEL_PATH, local_files_only=True)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.pad_token_id = tokenizer.eos_token_id

tokenizer.clean_up_tokenization_spaces = False
model.eval()

# 🧩 Cargar sft_data.jsonl en memoria
print(f"📚 Cargando dataset SFT desde:\n{SFT_DATA_PATH}\n")
sft_pairs = []

with open(SFT_DATA_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        prompt = " ".join(obj["prompt"]) if isinstance(obj["prompt"], list) else str(obj["prompt"])
        response = " ".join(obj["response"]) if isinstance(obj["response"], list) else str(obj["response"])
        sft_pairs.append((prompt, response))

prompts_list = [p for p, _ in sft_pairs]


def get_sft_response(user_input: str) -> str:
    """
    Devuelve la respuesta del sft_data más cercana al input del usuario.
    No genera texto nuevo, solo usa el dataset.
    """
    if not prompts_list:
        return "No hay datos en el dataset SFT."

    # Buscar la pregunta más parecida
    matches = difflib.get_close_matches(user_input, prompts_list, n=1, cutoff=0.4)
    if not matches:
        return "No tengo una respuesta en mi dataset para esa pregunta."

    best_prompt = matches[0]
    # Buscar la respuesta asociada
    for p, r in sft_pairs:
        if p == best_prompt:
            return r

    return "No tengo una respuesta en mi dataset para esa pregunta."


def generate_response(user_input: str) -> str:
    # Aquí SOLO usamos el dataset SFT
    return get_sft_response(user_input)


if __name__ == "__main__":
    print("🤖 Chatbot listo (modo SFT puro). Escribe 'salir' para terminar.\n")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            break
        response = generate_response(user_input)
        print("🤖", response)
