import os
from flask import Flask, render_template, request, jsonify
from worker import process_document, process_prompt

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_pdf():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    process_document(file_path)
    return jsonify({"message": "Documento procesado correctamente"})


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    answer = process_prompt(prompt)

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
