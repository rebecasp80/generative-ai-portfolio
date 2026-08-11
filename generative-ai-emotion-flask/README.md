# 🧠 Emotion AI — Modern Generative AI Emotion Detection  

Detector de emociones con **BERT**, **LoRA**, **QLoRA** y **Adapters**, integrado en una aplicación web moderna con **Flask** y una interfaz visual estilo *Glass UI*.

Este proyecto forma parte del portafolio profesional de Ingeniería de IA Generativa y demuestra el uso de **PEFT (Parameter‑Efficient Fine‑Tuning)** para adaptar modelos Transformer de forma eficiente.

---

## 🚀 Descripción del Proyecto

Este proyecto implementa un detector de emociones basado en **modelos Transformer (BERT)** que analiza texto y devuelve las probabilidades de seis emociones principales:

- **Anger**
- **Fear**
- **Joy**
- **Love**
- **Sadness**
- **Surprise**

Además, identifica la **emoción dominante**.  
La aplicación expone un endpoint web mediante **Flask**, incluye **pruebas unitarias**, manejo de errores y cumple con estándares de calidad de código (Pylint).

---

## 🚀 Características Principales

### 🧠 Modelos disponibles

- **BERT Base** — sin fine‑tuning  
- **LoRA** — entrenamiento eficiente con matrices de bajo rango  
- **QLoRA** — versión cuantizada en 4‑bit para despliegue ligero  
- **Adapter Pfeiffer** — capas entrenables insertadas en el modelo base  

### 🎨 Interfaz moderna

- Diseño **Glass UI + Neumorphism**  
- Barras animadas de probabilidad  
- Selector de modelo  
- Totalmente responsive  
- Sin dependencias externas  

### 🔧 Backend profesional

- Flask  
- API REST  
- Preprocesado NLP  
- Manejo de errores  
- Pruebas unitarias  
- Código limpio y modular  

---

## 🧠 Tecnologías Utilizadas

- Python 3  
- Flask  
- Transformers (Hugging Face)  
- PyTorch  
- Scikit-learn  
- Unittest
- Pylint  
- Git & GitHub  

---

## 📁 Estructura del Proyecto

generative-ai-emotion-flask/

│

├── app/

│   ├── init.py

│   ├── routes.py

│   └── templates/

│       └── index.html   ← Interfaz moderna

│

├── EmotionDetection/

│   ├── init.py

│   ├── bert_emotion_model.py   ← Carga Base / LoRA / QLoRA / Adapter

│   ├── preprocess.py

│   └── utils.py

│

├── training/

│   ├── train_lora.py

│   ├── train_qlora.py

│   ├── train_adapter.py

│   └── evaluate_models.py

│

├── models/

│   ├── base/

│   ├── lora/

│   ├── qlora/

│   └── adapter/

│

├── data/

│   └── emotions.csv

│

├── tests/

│   ├── test_api.py

│   └── test_emotion_detection.py

│

├── license

├── .gitignore

├── server.py

├── requirements.txt

└── README.md

---

## ⚙️ Instalación y Ejecución

### 1️⃣ Activar entorno virtual

C:\IA\venv310\Scripts\Activate.ps1

2️⃣ Instalar dependencias

pip install -r requirements.txt

3️⃣ Ejecutar la aplicación Flask

python server.py
La aplicación estará disponible en:
http://127.0.0.1:5000/

---

## 🧪 Entrenamiento de Modelos PEFT

El proyecto incluye scripts completos para entrenar:

✔ LoRA

python training/train_lora.py

Genera:

models/lora/

 ├── adapter_config.json
 
 ├── adapter_model.bin
 
 └── training_args.bin

✔ QLoRA

python training/train_qlora.py

Genera:

models/qlora/

 ├── adapter_config.json
 
 ├── adapter_model.bin
 
 └── training_args.bin

✔ Adapter Pfeiffer

python training/train_adapter.py

Genera:

models/adapter/
 
 ├── emotion_adapter/
 
 └── adapter_config.json

---

## 🧪 Pruebas Unitarias

Ejecutar las pruebas:
python -m unittest discover -s tests -p "test_*.py" -v


Las pruebas validan:
- Respuesta correcta del endpoint GET
- Respuesta correcta del endpoint POST
- Estructura del JSON
- Manejo de errores (texto vacío, JSON inválido, campo faltante)
- Preprocesado del texto
- Mapeo de etiquetas a emociones

---

## 🛡️ Manejo de Errores

La aplicación incluye:
- Validación de texto vacío
- Manejo de errores HTTP 400
- Respuestas limpias y consistentes para la interfaz web
- Sanitización del texto antes de enviarlo al modelo

---

## 📊 Evaluación de Modelos

Ejecuta:

python training/evaluate_models.py

Obtendrás métricas comparativas:

Accuracy
F1‑Score
Reporte por clase
Comparación Base vs LoRA vs QLoRA vs Adapter

---

## 🎨 Interfaz Moderna

La interfaz se encuentra en:

app/templates/index.html

Incluye:

Selector de modelo
Barras animadas
Emoción dominante
Diseño Glass UI
Compatible con móviles

---

## 📌 Aprendizajes Clave

Fine‑Tuning eficiente con LoRA, QLoRA y Adapters

Cuantización 4‑bit con bitsandbytes

Integración de PEFT en modelos Transformer

Desarrollo backend profesional con Flask

Interfaz moderna con HTML + CSS + JS

Pruebas unitarias y buenas prácticas de código

---

## 🧩 Funcionalidades Principales

- API REST para análisis emocional
- Modelo BERT sin fine‑tuning (predicción directa)
- Formato de salida limpio y estructurado
- Interfaz web simple y funcional
- Suite de pruebas unitarias completa
- Código validado con Pylint (10/10)

---

## 📌 Aprendizajes Clave

- Implementación de modelos Transformer
- Desarrollo backend con Flask
- Buenas prácticas de empaquetado Python
- Pruebas unitarias profesionales
- Manejo de errores y validación de entradas
- Control de versiones con Git y GitHub

---

## 👩‍💻 Autora

Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional de Ingeniería de IA generativa.

---

## 🪄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

Consulta el archivo LICENSE para más detalles.
