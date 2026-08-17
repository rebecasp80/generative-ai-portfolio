# 🤖 Generative AI portfolio

Colección profesional de **10 aplicaciones funcionales de IA Generativa, Procesamiento del Lenguaje Natural (NLP) y Deep Learning** desarrolladas en Python.

El repositorio abarca desde el entrenamiento local con Supervised Fine-Tuning (**SFT**) y **PEFT** (**LoRA**, **QLoRA 4-bit**) sobre Transformers, hasta arquitecturas **RAG corporativas**, traducción **Seq2Seq** desde cero en PyTorch, visión por computador, asistentes de voz multilingües y análisis de reuniones en tiempo real.

---

## 🧩 Proyectos incluidos

### 1. 🛩️ Aircraft Damage Captioning

Sistema de *captioning* para detección y descripción de daños en aeronaves mediante BLIP y VGG16, orientado a la inspección visual industrial asistida por IA.  

`Python` · `BLIP` · `VGG16` · `Hugging Face` · `Computer Vision`

### 2. 🌍 Babel Voice Assistant

Traductor de voz multilingüe en tiempo real con detección automática de idioma, Speech-to-Text (STT) y Text-to-Speech (TTS) integrado en interfaz web.  

`Python` · `Flask` · `LangChain` · `Groq` · `Web Speech API` · `HTML/CSS/JS`

### 3. 📄 Chatbot RAG para PDFs (`build-chatbot-for-your-data`)

Asistente conversacional RAG que responde sobre documentos PDF privados utilizando embeddings vectoriales, LangChain y Groq como motor de inferencia ultra-rápido. 

`Python` · `Flask` · `LangChain` · `Groq` · `RAG` · `FAISS / VectorStores`

### 4. 💬 Chatbot Transformers — Modelo Local Entrenado (GPT-Neo-125M + SFT)
Chatbot conversacional con arquitectura 100% offline basado en un modelo GPT-Neo-125M entrenado localmente mediante Supervised Fine-Tuning (SFT). Incluye pipeline de entrenamiento SFT, respuestas estructuradas por dataset, interfaz por consola y aplicación web Flask con modo oscuro.

`Python` · `PyTorch` · `Hugging Face Transformers` · `SFT` · `Flask` · `HTML/CSS/JS`

### 5. 🎙️ Enterprise Meeting Companion

Plataforma de análisis de reuniones corporativas que realiza transcripción automática multilingüe con Whisper y genera resúmenes ejecutivos procesables con Groq Llama 3.1.  

`Python` · `Gradio` · `Whisper` · `Groq` · `Docker`

### 6. 🧠 Emotion AI — Modern GenAI & PEFT Emotion Detection

Detector de emociones con modelos Transformer (BERT Base) optimizado mediante **PEFT (Parameter-Efficient Fine-Tuning)**: **LoRA**, **QLoRA (cuantización a 4-bit)** y **Adapters Pfeiffer**. Incluye API REST en Flask, frontend moderno estilo *Glass UI*, suite de pruebas unitarias (`unittest`), evaluación comparativa de métricas (F1/Accuracy) y código validado con Pylint (10/10).  

`Python` · `PyTorch` · `Hugging Face` · `PEFT (LoRA/QLoRA)` · `bitsandbytes` · `Flask` · `Unittest` · `Pylint`

### 7. 🌐 Generative AI Multilingual Chatbot

Tutor de idiomas y chatbot multilingüe con Groq, LangChain y FastAPI. Traduce, corrige gramática en tiempo real y ofrece salida de voz interactiva.  

`Python` · `FastAPI` · `LangChain` · `Groq` · `Web Speech API` · `HTML/CSS/JS`

### 8. 🖼️ Generative AI Vision — Image Captioning

Generador de descripciones automáticas de imágenes basado en el modelo BLIP. Interfaz en Gradio, empaquetado en contenedor Docker y desplegado en producción sobre IBM Cloud Code Engine.  

`Python` · `BLIP` · `Gradio` · `Hugging Face` · `Docker` · `IBM Cloud`

### 9. 🗣️ Generative AI Voice Assistant

Asistente de voz conversacional con capacidad de escucha activa, traducción simultánea e interpretación de contexto en múltiples idiomas.  

`Python` · `Flask` · `LangChain` · `Groq` · `Web Speech API`

### 10. 🔤 Generative AI Seq2Seq Translator (German → English)

Traductor automático basado en una arquitectura Encoder-Decoder Recurrente (GRU) entrenada **desde cero en PyTorch**. Pipeline completo de NLP con tokenización personalizada, gestión de vocabulario, evaluación mediante métricas BLEU e interfaz interactiva en Gradio.

`Python` · `PyTorch` · `GRU` · `Seq2Seq` · `Gradio` · `BLEU Metric`

---

## 🚀 Stack tecnológico

| Capa | Tecnologías |
| --- | --- |
| **Modelos & LLMs** | GPT-Neo · BERT · Llama 3.1 · BLIP · Whisper · Sentence Transformers · VGG16 · GRU (Seq2Seq) |
| **Técnicas de IA & Fine-Tuning** | Supervised Fine-Tuning (SFT) · PEFT (LoRA, QLoRA 4-bit, Adapters) · RAG · Quantization · Prompt Engineering |
| **Frameworks de IA** | PyTorch · Hugging Face Transformers · PEFT · bitsandbytes · LangChain 1.x · FAISS |
| **Motores de Inferencia** | Groq LPU Accelerators · PyTorch Native Engine |
| **Backend & APIs** | Python 3.10+ · Flask · FastAPI · Gradio · REST APIs |
| **Frontend & UI** | HTML5 · CSS3 (Glassmorphism & Dark Mode) · JavaScript · Web Speech API |
| **Calidad & Testing** | Unittest · Pylint (10/10) · Preprocesamiento NLP & Tokenización |
| **DevOps & Cloud** | Docker · Git & GitHub · IBM Cloud Code Engine |

---

## 📁 Estructura del repositorio

generative-ai-apps/

│

├── README.md

├── LICENSE

├── aircraft-damage-captioning/

├── babel-voice-assistant/

├── build-chatbot-for-your-data/

├── chatbot-transformers/

├── enterprise-meeting-companion/

├── generative-ai-emotion-flask/

├── generative-ai-multilingual-chatbot/

├── generative-ai-seq2seq-translator/

├── generative-ai-vision-python/

└── generative-ai-voice-assistant/

---

## 👩‍💻 Autora

Desarrollado por **Rebeca Soto** como parte de su portafolio profesional de IA generativa y transformación digital.

🔗 [linkedin.com/in/rebeca-soto-ai](https://linkedin.com/in/rebeca-soto-ai)

🔗 [github.com/rebecasp80](https://github.com/rebecasp80)

---

## 🪄 Licencia

Distribuido bajo licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.
