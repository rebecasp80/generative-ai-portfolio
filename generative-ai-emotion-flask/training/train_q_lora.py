import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model
import torch

# 1. Cargar dataset local
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

# 3. Configuración QLoRA (cuantización 4-bit)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.float16
)

# 4. Modelo base cuantizado
model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=6,
    quantization_config=bnb_config,
    device_map="auto"
)

# 5. Configuración LoRA sobre modelo cuantizado
lora_config = LoraConfig(
    r=4,
    lora_alpha=8,
    target_modules=["query", "value"],
    lora_dropout=0.05,
    bias="none",
    task_type="SEQ_CLS"
)

model = get_peft_model(model, lora_config)

# 6. Entrenamiento
training_args = TrainingArguments(
    output_dir="models/qlora/",
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

# 7. Guardar modelo QLoRA
model.save_pretrained("models/qlora/")
print("✅ Modelo QLoRA guardado en /models/qlora/")
