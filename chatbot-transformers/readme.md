# 🤖 Chatbot Transformers — Modelo Local Entrenado (GPT‑Neo‑125M + SFT + DPO)

Este proyecto implementa un chatbot moderno utilizando un modelo de lenguaje entrenado localmente con SFT + Reward Model + DPO, basado en GPT‑Neo‑125M.

Incluye un chatbot por consola y un pipeline completo de entrenamiento.

---

## 🚀 Características principales

- **Modelo local GPT‑Neo‑125M fine‑tuned con SFT + DPO**  

- **Entrenamiento completo RLHF (SFT → Reward → DPO)**  
  
- **Chatbot por consola (chatbot_pipeline.py)**  

- **Dataset ampliado con 200 ejemplos DPO**  

- **Arquitectura totalmente offline (sin API externa)**

---

## 📁 Estructura del proyecto

chatbot-transformers/
│
├── training/
│   ├── sft_trainer.py
│   ├── reward_trainer.py
│   ├── dpo_trainer.py
│   ├── dpo_model_neo/        # Modelo entrenado (GPT‑Neo‑125M fine‑tuned)
│   └── dataset_loader.py
│
├── data/
│   ├── sft.jsonl             # Dataset SFT
│   ├── preferences.jsonl     # Dataset DPO ampliado (200 ejemplos)
│   └── reward.jsonl          # Dataset del reward model
│
├── chatbot_pipeline.py        # Chatbot por consola
│
└── README.md

---

## 🔧 Requisitos

Instala las dependencias dentro de tu entorno virtual:

pip install transformers torch datasets

---

## ▶️ Ejecutar el chatbot

Desde la carpeta chatbot-transformers

Entrenar el modelo:

python -m training.dpo_trainer

Ejecutar el chatbot:

python chatbot_pipeline.py

---

## 📌 Objetivo del proyecto

Este módulo forma parte del repositorio Generative AI Apps, donde se construyen modelos de IA generativa entrenados desde cero con técnicas RLHF.

---

## 🧩 Instalación rápida

git clone https://github.com/<tu_usuario>/chatbot-transformers.git
cd chatbot-transformers
python -m venv venv310
source venv310/bin/activate  # o venv310\\Scripts\\activate en Windows
pip install -r requirements.txt
python app.py


---

## 👩‍💻 Autora

Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional de Ingeniería de IA generativa con modelos locales, Python y Transformers.

---

## 📄 Licencia
Este proyecto está bajo la licencia incluida en el repositorio principal.