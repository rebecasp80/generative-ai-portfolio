import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel
from sklearn.metrics import classification_report
import torch

label2id = {"anger":0, "fear":1, "joy":2, "love":3, "sadness":4, "surprise":5}
id2label = {v:k for k,v in label2id.items()}

# Dataset local
df = pd.read_csv("data/emotions.csv")
df["labels"] = df["label"].map(label2id)
dataset = Dataset.from_pandas(df)

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=128)

dataset = dataset.map(tokenize, batched=True)
dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

def evaluate(model, name):
    preds = []
    trues = []

    for item in dataset:
        inputs = {
            "input_ids": item["input_ids"].unsqueeze(0),
            "attention_mask": item["attention_mask"].unsqueeze(0)
        }

        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
            pred = torch.argmax(probs).item()

        preds.append(pred)
        trues.append(item["labels"])

    print(f"\n📊 Resultados del modelo: {name}")
    print(classification_report(trues, preds, target_names=list(label2id.keys())))

# Base
base_model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=6)
evaluate(base_model, "base")

# LoRA
lora_model = PeftModel.from_pretrained(
    AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=6),
    "models/lora/"
)
evaluate(lora_model, "lora")

# QLoRA
qlora_model = PeftModel.from_pretrained(
    AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=6),
    "models/qlora/"
)
evaluate(qlora_model, "qlora")

# Adapter
adapter_model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=6)
adapter_model.load_adapter("models/adapter/")
adapter_model.set_active_adapters("emotion_adapter")
evaluate(adapter_model, "adapter")
