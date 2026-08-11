from flask import Blueprint, request, jsonify, render_template
from EmotionDetection.bert_emotion_model import EmotionModel
from EmotionDetection.preprocess import clean_text
from EmotionDetection.utils import map_label_to_emotion

bp = Blueprint("routes", __name__)

# Modelo por defecto: base
emotion_model = EmotionModel(model_type="base")


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """
    Endpoint principal para detección de emociones.
    Permite elegir el modelo: base, lora, qlora, adapter.
    Ejemplo:
        /emotionDetector?textToAnalyze=hola&model=lora
    """
    # Obtener texto
    if request.method == "GET":
        text_to_analyze = request.args.get("textToAnalyze", "")
        model_type = request.args.get("model", "base")
    else:
        data = request.get_json() or {}
        text_to_analyze = data.get("textToAnalyze", "")
        model_type = data.get("model", "base")

    # Validación
    if not text_to_analyze.strip():
        return jsonify({"error": "¡Texto inválido! Por favor, intenta de nuevo."}), 400

    # Cargar modelo solicitado
    global emotion_model
    emotion_model = EmotionModel(model_type=model_type)

    # Preprocesado
    cleaned_text = clean_text(text_to_analyze)

    # Predicción
    label, probs = emotion_model.predict(cleaned_text)
    emotion = map_label_to_emotion(label)

    # Respuesta
    return jsonify({
        "model_used": model_type,
        "text": text_to_analyze,
        "emotion": emotion,
        "probabilities": probs,
        "response": (
            f"Para la declaración dada, la respuesta del sistema es: "
            f"'anger': {probs[0][0]:.3f}, 'fear': {probs[0][1]:.3f}, "
            f"'joy': {probs[0][2]:.3f}, 'love': {probs[0][3]:.3f}, "
            f"'sadness': {probs[0][4]:.3f}, 'surprise': {probs[0][5]:.3f}. "
            f"La emoción dominante es **{emotion}** usando el modelo **{model_type}**."
        )
    })


@bp.route("/availableModels", methods=["GET"])
def available_models():
    """
    Lista los modelos disponibles en /models/
    """
    models = emotion_model.available_models()
    return jsonify({"available_models": models})
