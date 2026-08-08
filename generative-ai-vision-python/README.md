# 🖼️ Generative AI Vision — Image Captioning App (BLIP + Gradio)

Aplicación de **IA generativa** que utiliza el modelo **BLIP (Bootstrapped Language-Image Pretraining)** para generar descripciones automáticas de imágenes.  
La interfaz está construida con **Gradio**, y el proyecto está completamente **contenedorizado con Docker** para facilitar su despliegue en entornos cloud.

---

## 🚀 Características principales

- 🧠 **Modelo BLIP** para generación de subtítulos de imágenes.
- 🎨 **Interfaz Gradio** intuitiva y fácil de usar.
- 🐳 **Contenedor Docker** listo para producción.
- 📸 Soporte para carga de imágenes locales.

---

## 📂 Estructura del proyecto

generative-ai-vision-python/

│

├── src/

│   ├── screenshots/

│   │   ├── app_running.png

│   │   └── app_interface_demo.png

│   ├── blip_caption.py

│   └── image_captioning_app.py

│

├── images/

│   └── ejemplo.jpg

├── notebooks/

├── Dockerfile

├── requirements.txt

└── README.md

---

## 🧠 Modelo utilizado
Salesforce/blip-image-captioning-base  
El modelo se descarga automáticamente desde Hugging Face al iniciar la aplicación.

---

## 🛠️ Instalación y ejecución local
Desde la carpeta del proyecto:

cd generative-ai-vision-python
python -m venv venv
venv\Scripts\activate      # En Windows
pip install -r requirements.txt
python src/image_captioning_app.py

La interfaz estará disponible en:

http://127.0.0.1:7860

---

## 🐳 Ejecución con Docker

cd generative-ai-vision-python
docker build -t blip-gradio-app .
docker run -p 7860:7860 blip-gradio-app

---

## 👩‍💻 Autora
Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional de Ingeniería de IA generativa.

---

## 🪄 Licencia
Este proyecto se distribuye bajo la licencia MIT.

Consulta el archivo LICENSE para más detalles.
