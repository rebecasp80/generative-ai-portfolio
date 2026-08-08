from flask import Blueprint, request, jsonify, render_template
from EmotionDetection.bert_emotion_model import EmotionModel
from EmotionDetection.preprocess import clean_text
from EmotionDetection.utils import map_label_to_emotion

bp = Blueprint("routes", __name__)
emotion_model = EmotionModel()

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    if request.method == "GET":
        text_to_analyze = request.args.get("textToAnalyze", "")
    else:
        data = request.get_json() or {}
        text_to_analyze = data.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return jsonify({"error": "¡Texto inválido! Por favor, intenta de nuevo."}), 400

    cleaned_text = clean_text(text_to_analyze)
    label, probs = emotion_model.predict(cleaned_text)
    emotion = map_label_to_emotion(label)

    return jsonify({
        "text": text_to_analyze,
        "emotion": emotion,
        "probabilities": probs,
        "response": (
            f"Para la declaración dada, la respuesta del sistema es: "
            f"'anger': {probs[0][0]:.3f}, 'fear': {probs[0][1]:.3f}, "
            f"'joy': {probs[0][2]:.3f}, 'love': {probs[0][3]:.3f}, "
            f"'sadness': {probs[0][4]:.3f}, 'surprise': {probs[0][5]:.3f}. "
            f"La emoción dominante es **{emotion}**."
        )
    })
