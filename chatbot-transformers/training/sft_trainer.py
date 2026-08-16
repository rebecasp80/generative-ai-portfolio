import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
import os

# 🧠 Rutas
BASE_PATH = os.path.join(os.path.dirname(__file__), "neo_base")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "sft_model_neo")
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sft_data.jsonl")

print("🔧 Cargando modelo base GPT‑Neo‑125M...")
tokenizer = AutoTokenizer.from_pretrained(BASE_PATH, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(BASE_PATH, local_files_only=True)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.pad_token_id = tokenizer.eos_token_id

print("📚 Cargando dataset SFT...")
dataset = load_dataset("json", data_files=DATA_PATH, split="train")

def to_text(x):
    return " ".join(x) if isinstance(x, list) else str(x)

def preprocess(example):
    prompt = to_text(example["prompt"])
    response = to_text(example["response"])
    text = f"Usuario: {prompt}\nAsistente: {response}"

    enc = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=256
    )

    enc["labels"] = enc["input_ids"].copy()
    return enc

print("🔄 Tokenizando dataset...")
tokenized = dataset.map(preprocess, batched=False)

# Convertir a tensores
def collate_fn(batch):
    return {
        "input_ids": torch.tensor([item["input_ids"] for item in batch]),
        "attention_mask": torch.tensor([item["attention_mask"] for item in batch]),
        "labels": torch.tensor([item["labels"] for item in batch]),
    }

loader = DataLoader(tokenized, batch_size=4, shuffle=True, collate_fn=collate_fn)

optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

print("🚀 Entrenando SFT con batching real...")

model.train()

for epoch in range(3):
    print(f"\n🟣 Epoch {epoch+1}/3")
    total_loss = 0

    for batch in loader:
        outputs = model(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            labels=batch["labels"]
        )

        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        total_loss += loss.item()

    print(f"🔥 Loss epoch {epoch+1}: {total_loss / len(loader):.4f}")

print("\n💾 Guardando modelo SFT...")
model.save_pretrained(OUTPUT_PATH)
tokenizer.save_pretrained(OUTPUT_PATH)

print("✅ Entrenamiento SFT completado")
