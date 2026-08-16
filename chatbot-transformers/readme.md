# 🤖 Chatbot Transformers — Modelo Local Entrenado (GPT‑Neo‑125M + SFT)

Este proyecto implementa un chatbot moderno utilizando un modelo de lenguaje GPT‑Neo‑125M entrenado localmente con **Supervised Fine‑Tuning (SFT)** y un **chatbot que responde exclusivamente con las respuestas del dataset SFT**, sin usar APIs externas.

Incluye:
- un chatbot por consola
- una interfaz web moderna en Flask (modo oscuro)
- el pipeline básico de entrenamiento SFT

---

## 🚀 Características principales

- **Modelo local GPT‑Neo‑125M fine‑tuned con SFT** 
  
- **Chatbot por consola (chatbot_pipeline.py)**  

- **Interfaz web Flask en modo oscuro (`app.py`)**

- **Respuestas basadas únicamente en el dataset SFT (`sft_data.jsonl`)**  

- **Arquitectura totalmente offline (sin API externa)**  

> Nota: Aunque existen scripts relacionados con reward/DPO en la carpeta `training/`, la versión actual del proyecto **no utiliza DPO ni reward model en producción**. El chatbot funciona en modo **SFT puro + recuperación de respuestas del dataset**.

---

## 📁 Estructura del proyecto

chatbot-transformers/

│

├── training/

│   ├── sft_trainer.py        # Entrenamiento SFT del modelo GPT‑Neo‑125M

│   ├── reward_trainer.py     # (Opcional / experimental, no usado en la versión actual)

│   ├── dpo_trainer.py        # (Opcional / experimental, no usado en la versión actual)

│   └── dataset_loader.py     # Utilidades para cargar datasets

│

├── data/

│   ├── sft_data.jsonl        # Dataset SFT (pares pregunta–respuesta)

│   └── preferences.jsonl     # (Opcional / experimental)

│

├── chatbot_pipeline.py       # Lógica del chatbot (modo SFT puro, usa sft_data.jsonl)

├── app.py                    # Interfaz web Flask en modo oscuro

├── requirements.txt

└── README.md

---

## 🔧 Requisitos

Instala las dependencias dentro de tu entorno virtual:

pip install transformers torch datasets flask

---

## ▶️ Ejecutar el chatbot

Desde la carpeta chatbot-transformers:

- Chatbot por consola (modo SFT puro)

python chatbot_pipeline.py

- Interfaz web Flask (modo oscuro)

python app.py

- Luego abre en el navegador:

http://127.0.0.1:5000

---

## 📌 Objetivo del proyecto

Este módulo forma parte del repositorio Generative AI Apps, donde se construyen modelos de IA generativa entrenados localmente con SFT y se exploran técnicas RLHF de forma experimental, manteniendo siempre una arquitectura offline y reproducible.

---

## 🧩 Instalación rápida

git clone https://github.com/<tu_usuario>/chatbot-transformers.git

cd chatbot-transformers


python -m venv venv310

# Windows
venv310\Scripts\activate

# Linux/Mac
source venv310/bin/activate


pip install -r requirements.txt


python app.py


---

## 👩‍💻 Autora

Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional de Ingeniería de IA generativa con modelos locales, Python y Transformers.

---

## 📄 Licencia
Este proyecto está bajo la licencia incluida en el repositorio principal.