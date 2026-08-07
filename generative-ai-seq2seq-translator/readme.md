# 🧠 Generative AI — Seq2Seq Translator (German → English)

Aplicación de IA generativa que implementa un modelo Seq2Seq con Encoder–Decoder (GRU) para traducir frases del alemán al inglés.

Incluye un pipeline completo de NLP, entrenamiento desde cero, evaluación con BLEU, y una interfaz visual construida con Gradio.

Este proyecto forma parte del portafolio profesional de Ingeniería de IA generativa, siguiendo buenas prácticas de arquitectura, modularidad y reproducibilidad.

---

## 🚀 Características principales

🔤 Modelo Seq2Seq entrenado desde cero con GRU.

📚 Dataset personalizado con más de 650 pares alemán ↔ inglés.

🧪 Evaluación BLEU para medir la calidad de las traducciones.

🎛️ Interfaz Gradio para probar el modelo en tiempo real.

🧩 Arquitectura modular: dataset, vocabulario, modelo, entrenamiento, evaluación y app.

⚙️ Entrenamiento configurable (épocas, ratio de teacher forcing, tamaño de embedding, etc.).

💾 Checkpoints automáticos y guardado del mejor modelo.

---

## 📂 Estructura del proyecto

generative-ai-seq2seq-translator/

│

├── data/

│   ├── raw/

│   │   └── de_en_samples.txt

│   └── processed/

│       ├── vocab_de.pkl

│       └── vocab_en.pkl

│

├── models/

│   ├── checkpoints/

│   │   ├── seq2seq_epoch_1.pt

│   │   ├── seq2seq_epoch_2.pt

│   │   └── ...

│   └── best_model.pt

│

├── src/

│   ├── app_gradio.py

│   ├── config.py

│   ├── dataset.py

│   ├── evaluate.py

│   ├── models.py

│   ├── train.py

│   ├── translate.py

│   └── vocab.py

│

├── screenshots/

│   ├── app_running.png

│   └── translation_demo.png

│

├── requirements.txt

└── README.md

---

## 🧠 Modelo utilizado

🔸 Arquitectura Seq2Seq (Encoder–Decoder)

Encoder: GRU con embeddings aprendidos.

Decoder: GRU con capa lineal para distribución de probabilidad.

Teacher forcing: configurable (0.5–0.7 recomendado).

Tokenización: vocabulario propio con <SOS>, <EOS>, <PAD>.

🔸 Entrenamiento

200 épocas recomendadas.

Checkpoints por época.

Guardado automático del mejor modelo.

Optimización con Adam.

---

## 🛠️ Instalación y ejecución local

1. Crear entorno virtual

cd generative-ai-seq2seq-translator

python -m venv venv310

venv310\Scripts\activate

pip install -r requirements.txt

2. Entrenar el modelo

python -m src.train

El modelo final se guardará en:

models/best_model.pt

3. Ejecutar la aplicación Gradio

python -m src.app_gradio

La interfaz estará disponible en:

http://127.0.0.1:7860

---

## 🎨 Interfaz Gradio

La app permite:

Introducir una frase en alemán.

Obtener la traducción generada por el modelo.

Visualizar resultados en tiempo real.

Ejemplo:

Eingabe: ein hund schläft

Ausgabe: a dog is sleeping

---

## 📊 Métricas BLEU

El proyecto incluye una función de evaluación BLEU:

from src.evaluate import calculate_bleu_score

Permite medir la calidad de las traducciones comparando hipótesis vs. referencias.

---

## 📘 Dataset

El dataset contiene:

Más de 650 pares alemán ↔ inglés.

Frases de niveles A1–C1.

Estructuras simples, compuestas y complejas.

Temáticas variadas: viajes, trabajo, emociones, tecnología, vida diaria.

Puedes ampliarlo fácilmente editando:

data/raw/de_en_samples.txt

---

## 👩‍💻 Autora

Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional de Ingeniería de IA generativa, con enfoque en modelos de lenguaje, NLP y aplicaciones interactivas.

---

## 🪄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

Consulta el archivo LICENSE para más detalles.