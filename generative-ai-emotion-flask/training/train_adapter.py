import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments, AdapterConfig
import torch

# 1. Dataset local
df = pd.read_csv("data/emotions.csv")

label2id = {"anger":0, "fear":1, "joy":2, "love":3, "sadness":4, "surprise":5}
df["labels"] = df["label"].map(label2id)

dataset = Dataset.from_pandas(df)

# 2. Tokenizador
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=128)

dataset = dataset.map(tokenize, batched=True)
dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

# 3. Modelo base
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=6)

# 4. Configuración Adapter
adapter_config = AdapterConfig.load("pfeiffer", reduction_factor=16)

model.add_adapter("emotion_adapter", config=adapter_config)
model.train_adapter("emotion_adapter")

# 5. Entrenamiento
training_args = TrainingArguments(
    output_dir="models/adapter/",
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

# 6. Guardar Adapter
model.save_adapter("models/adapter/", "emotion_adapter")
print("✅ Adapter guardado en /models/adapter/")
