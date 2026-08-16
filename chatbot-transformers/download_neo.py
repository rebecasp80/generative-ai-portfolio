from transformers import AutoTokenizer, AutoModelForCausalLM

print("🔧 Descargando modelo GPT‑Neo‑125M...")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")

model.save_pretrained("training/neo_base")
tokenizer.save_pretrained("training/neo_base")

print("✅ GPT‑Neo‑125M descargado y guardado correctamente en training/neo_base")
