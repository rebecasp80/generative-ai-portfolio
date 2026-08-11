import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model
import torch

# 1. Cargar dataset local
df = pd.read_csv("data/emotions.csv")

# Mapear etiquetas a números
label2id = {"anger":0, "fear":1, "joy":2, "love":3, "sadness":4, "surprise":5}
df["labels"] = df["label"].map(label2id)

dataset = Dataset.from_pandas(df)

# 2. Tokenizador
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=128)

dataset = dataset.map(tokenize, batched=True)
dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

# 3. Configuración LoRA
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["query", "value"],
    lora_dropout=0.1,
    bias="none",
    task_type="SEQ_CLS"
)

# 4. Modelo base + LoRA
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=6)
model = get_peft_model(model, lora_config)

# 5. Entrenamiento
training_args = TrainingArguments(
    output_dir="models/lora/",
    per_device_train_batch_size=4,
    num_train_epochs=5,
    logging_steps=10,
    save_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

trainer.train()

# 6. Guardar modelo LoRA
model.save_pretrained("models/lora/")
print("✅ Modelo LoRA guardado en /models/lora/")
