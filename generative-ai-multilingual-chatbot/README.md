# 🤖 Generative AI Multilingual Chatbot — Asistente Conversacional con Groq + LangChain + FastAPI

Este proyecto implementa un chatbot multilingüe basado en Groq y LangChain 1.x, capaz de mantener conversaciones naturales, traducir automáticamente y adaptarse al tono y personalidad del usuario.

Incluye una interfaz web moderna con diseño tecnológico, animaciones suaves y soporte de voz para escuchar las respuestas en distintos idiomas.

Forma parte del repositorio **Generative AI Apps**, una colección de aplicaciones de IA generativa desarrolladas para portafolios profesionales.

---

## 🚀 Características principales

💬 **Chat multilingüe con Groq + LangChain**  
Responde en múltiples idiomas con traducción automática y coherencia contextual.

🧠 **Personalidad y tono adaptativos**  
El bot ajusta su estilo según el tono del usuario (amable, técnico, profesor, creativo, tutor de idiomas).

🌍 **Selector de idioma**  
Permite elegir el idioma de salida: Español, Inglés, Francés, Alemán, Italiano, Hindi y más.

🔊 **Síntesis de voz (TTS)**  
El asistente puede pronunciar las respuestas en el idioma seleccionado mediante la API de voz del navegador.

🎨 **Interfaz moderna**  
Diseño limpio con modo claro/oscuro, animaciones, avatares y burbujas estilizadas.

🧩 **Tutor de idiomas integrado**  
Corrige errores, explica gramática y ofrece ejemplos en el idioma elegido.

---

## ⚙️ Tecnologías utilizadas

- **Groq** — modelo `llama-3.1-8b-instant` para respuestas rápidas y naturales  
- **LangChain 1.x** — gestión de cadenas y razonamiento contextual  
- **FastAPI** — servidor backend eficiente  
- **HTML/CSS/JavaScript** — interfaz web interactiva  
- **SpeechSynthesis API** — lectura de respuestas en voz  
- **LocalStorage** — memoria persistente del chat

---

## 📁 Estructura del proyecto

generative-ai-multilingual-chatbot/
│
├── src/
│   ├── main.py             # Servidor FastAPI
│   ├── chat_engine.py      # Motor de conversación con Groq + LangChain
│   ├── model_loader.py     # Carga del modelo Groq
│   ├── tokenizer_utils.py  # Utilidades de tokenización
│
├── frontend/
│   └── index.html          # Interfaz web completa
│
├── static/
│   ├── style.css           # Estilos visuales
│   └── script.js           # Lógica del frontend
│
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Documentación del proyecto
└── .env.example            # Clave de API (sin datos reales)


---

## 🔧 Instalación y ejecución

Instala las dependencias dentro de tu entorno virtual:

pip install fastapi uvicorn langchain langchain-core langchain-community langchain-groq python-dotenv

Ejecuta el servidor:

uvicorn src.main:app --reload

Abre en tu navegador:

http://127.0.0.1:8000

---

## 📌 Objetivo del proyecto
Este chatbot demuestra el uso de IA generativa aplicada a la comunicación multilingüe, integrando:

Traducción automática

Adaptación de tono y personalidad

Interfaz moderna y accesible

Voz integrada para práctica de idiomas

---

## 👩‍💻 Autora
Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional de Ingeniería de IA generativa.
Repositorio: Generative AI Apps  
Tecnologías: Python, FastAPI, Groq, LangChain, HTML/CSS, JavaScript

---

## 🪄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

Consulta el archivo LICENSE para más detalles.