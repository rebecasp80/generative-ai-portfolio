# 🧠 Emotion Detection Web App — BERT Edition  

Aplicación web para detectar emociones en texto utilizando **BERT (Transformers)**.  
Incluye backend en Flask, empaquetado Python, pruebas unitarias, manejo de errores y análisis estático de código.

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

EmotionDetection/

    __init__.py
    
    bert_emotion_model.py
    
    preprocess.py
    
    utils.py

app/

    __init__.py
    
    routes.py
    
    templates/

tests/

    __init__.py
    
    test_emotion_detection.py
    
    test_api.py

docs/            tareas y documentación del desarrollo

server.py

requirements.txt

README.md

LICENSE

---

## ⚙️ Instalación y Ejecución

### 1️⃣ Activar entorno virtual

C:\IA\venv310\Scripts\Activate.ps1

2️⃣ Instalar dependencias

pip install -r requirements.txt

3️⃣ Ejecutar la aplicación Flask

python server.py
La aplicación estará disponible en:
http://127.0.0.1:5002/

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

## 📸 Capturas de Pantalla

✔ Despliegue de la aplicación

✔ Manejo de errores

✔ Resultados de predicción

Las imágenes están disponibles en la carpeta /screenshots

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
