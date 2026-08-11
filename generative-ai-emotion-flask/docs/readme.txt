🤖 Emotion Detection Web App (Generative AI with Python & Flask)

Aplicación web para detectar emociones en texto utilizando la API de Watson NLP.

Incluye backend en Flask, empaquetado Python, pruebas unitarias, manejo de errores y análisis estático de código.

Este proyecto forma parte del curso profesional de Ingeniería en IA Generativa, demostrando la integración práctica de modelos de lenguaje en aplicaciones web.

🚀 Descripción del Proyecto

El sistema implementa un detector de emociones basado en IA que analiza texto y devuelve las probabilidades de cinco emociones principales:

Anger

Disgust

Fear

Joy

Sadness

Además, identifica la emoción dominante y expone un endpoint web mediante Flask.

El proyecto incluye pruebas unitarias, manejo de errores y validación de calidad de código con Pylint (10/10).

🧠 Tecnologías Utilizadas

Python 3

Flask

Watson NLP API

Requests

Unittest

Pylint

Git & GitHub

📁 Estructura del Proyecto

plaintext

EmotionDetection/

init.py

emotion_detection.py

server.py

tests/

test_emotion_detection.py

screenshots/

6b_deployment_test.png 7c_error_handling_interface.png

requirements.txt

README.md

⚙️ Instalación y Ejecución

1️⃣ Clonar el repositorio

bash

git clone https://github.com/rebecasp80/oaqjp-final-project-emb-ai

cd oaqjp-final-project-emb-ai

2️⃣ Instalar dependencias

bash

pip install -r requirements.txt

3️⃣ Ejecutar la aplicación Flask

bash

python server.py

La aplicación estará disponible en:

👉 http://127.0.0.1:5000/

🧪 Pruebas Unitarias

Ejecutar las pruebas:

bash

python -m unittest discover

Las pruebas validan:

Formato de salida

Emoción dominante

Integración con la función principal

🛡️ Manejo de Errores

La aplicación incluye:

Validación de texto vacío

Manejo de errores HTTP 400 del servicio Watson

Respuestas limpias y consistentes para la interfaz web

📸 Capturas de Pantalla

✔ Despliegue de la aplicación

📂 /screenshots/6b_deployment_test.png

✔ Manejo de errores

📂 /screenshots/7c_error_handling_interface.png

🧩 Funcionalidades Principales

API REST para análisis emocional

Integración con Watson NLP

Formato de salida limpio y estructurado

Interfaz web simple y funcional

Código validado con Pylint (10/10)

📌 Aprendizajes Clave

Consumo de APIs de IA

Desarrollo backend con Flask

Buenas prácticas de empaquetado Python

Pruebas unitarias profesionales

Manejo de errores y validación de entradas

Control de versiones con Git y GitHub

👩‍💻 Autora

Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional en Inteligencia Artificial, Python y aplicaciones web.

🪄 Licencia
Este proyecto se distribuye bajo la licencia MIT.

Consulta el archivo LICENSE para más detalles.