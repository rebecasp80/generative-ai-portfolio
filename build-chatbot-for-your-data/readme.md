# 🤖 Chatbot Transformers — Flask + Groq + Interfaz Web

Este proyecto implementa un chatbot inteligente basado en RAG (Retrieval Augmented Generation) utilizando Groq como motor de inferencia, Flask como backend y una interfaz web moderna con modo oscuro, avatar y experiencia tipo ChatGPT.

Es parte del proyecto *Generative AI Apps*, donde se integran diferentes aplicaciones de IA generativa.

---

## 🚀 Características principales

- **Modelo de IA Groq**  

  - Inferencia ultrarrápida.

  - Respuestas coherentes y precisas basadas en el contenido del documento cargado.

  - Integración mediante ChatGroq.

- **Backend Flask**  

  - Rutas simples y eficientes.

  - Manejo de carga de documentos PDF.

  - Procesamiento RAG con embeddings + FAISS.

- **Interfaz web estilo ChatGPT**  

  - Modo oscuro profesional.

  - Avatar tipo chatbot (icono 🤖).

  - Burbujas de conversación.

  - Scroll automático.

  - Envío rápido de mensajes.  

- **Memoria de conversación**  

  - El chatbot mantiene el contexto mientras la sesión está activa.

  - Permite conversaciones fluidas sobre el documento cargado.

---

## 📁 Estructura del proyecto

chatbot-transformers/

│

├── app.py                 # Backend Flask + Groq

│

├── worker.py              # Pipeline RAG (PDF → Chunks → FAISS → Groq)

│

├── templates/

│   └── index.html         # Interfaz web del chatbot

│

└── static/

   ├── style.css          # Estilos (modo oscuro + diseño moderno)
    
   ├── script.js          # Lógica del frontend
    
   └── avatar.png         # Avatar del chatbot

---

## 🔧 Requisitos

Instala las dependencias dentro de tu entorno virtual:

pip install flask groq langchain faiss-cpu sentence-transformers

---

## 🔑 Configuración de la API de Groq

Crea un archivo .env en la raíz del proyecto:

Crea un archivo .env en la raíz del proyecto:

---

## ▶️ Ejecutar el chatbot

Desde la carpeta del proyecto:

python app.py

Luego abre en tu navegador:

http://127.0.0.1:5000

---

## 🧠 Rutas del servidor

GET /

Renderiza la interfaz web.

POST /upload

Carga un documento PDF y construye el índice FAISS.

POST /ask

Envía una pregunta y devuelve la respuesta generada por Groq usando RAG.

---

## 🎨 Interfaz web

La interfaz incluye:

- Modo oscuro

 Icono de usuario 🧑 y chatbot 🤖

- Burbujas de chat

- Scroll automático

- Envío rápido de mensajes

- Diseño limpio y profesional

---

## 📌 Objetivo del proyecto

Este módulo forma parte del repositorio Generative AI Apps, donde se construyen aplicaciones de IA generativa para mi portafolio profesional.

---

## 👩‍💻 Autora

Proyecto desarrollado por Rebeca Soto como parte de mi portafolio profesional de Ingeniería de IA generativa.

Proyecto: Generative AI Apps  

Tecnologías: Python · Flask · Groq · LangChain · FAISS · HTML/CSS · JavaScriptt

---

## 📄 Licencia

Este proyecto está bajo la licencia incluida en el repositorio principal.
