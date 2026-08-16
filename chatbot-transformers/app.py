from flask import Flask, request, render_template_string, redirect, url_for
from chatbot_pipeline import generate_response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Chatbot GPT‑Neo SFT</title>
    <style>
        :root {
            --bg-color: #121212;
            --card-color: #1e1e1e;
            --text-color: #e0e0e0;
            --user-bubble: #bb86fc;
            --bot-bubble: #03dac6;
            --accent-color: #bb86fc;
            --border-color: #333;
        }
        body.light {
            --bg-color: #f4f4f4;
            --card-color: #ffffff;
            --text-color: #222222;
            --user-bubble: #4b7bec;
            --bot-bubble: #20bf6b;
            --accent-color: #4b7bec;
            --border-color: #cccccc;
        }
        body {
            font-family: "Segoe UI", Arial, sans-serif;
            background: var(--bg-color);
            color: var(--text-color);
            padding: 20px;
            transition: background 0.3s ease, color 0.3s ease;
        }
        .chatbox {
            width: 800px;
            margin: auto;
            background: var(--card-color);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.6);
            transition: background 0.3s ease, box-shadow 0.3s ease;
        }
        h2 {
            margin-top: 0;
            color: var(--text-color);
        }
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .top-bar-buttons {
            display: flex;
            gap: 10px;
        }
        .msg-container {
            max-height: 420px;
            overflow-y: auto;
            margin-bottom: 20px;
            padding-right: 10px;
        }
        .message {
            display: flex;
            margin-bottom: 10px;
            animation: fadeIn 0.3s ease;
        }
        .message.user .bubble {
            background: var(--user-bubble);
            margin-left: auto;
            border-bottom-right-radius: 0;
        }
        .message.bot .bubble {
            background: var(--bot-bubble);
            margin-right: auto;
            border-bottom-left-radius: 0;
        }
        .bubble {
            max-width: 70%;
            padding: 10px 14px;
            border-radius: 16px;
            color: #121212;
            font-size: 14px;
            line-height: 1.4;
            position: relative;
        }
        .label {
            font-size: 11px;
            margin-bottom: 2px;
            opacity: 0.8;
        }
        textarea {
            width: 100%;
            border-radius: 8px;
            padding: 10px;
            border: 1px solid var(--border-color);
            background: transparent;
            color: var(--text-color);
            resize: vertical;
            min-height: 60px;
        }
        textarea::placeholder {
            color: #888;
        }
        button {
            padding: 8px 16px;
            border-radius: 8px;
            background: var(--accent-color);
            color: #121212;
            border: none;
            cursor: pointer;
            font-weight: 600;
            font-size: 13px;
        }
        button:hover {
            filter: brightness(1.1);
        }
        .bottom-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 10px;
        }
        .bottom-bar-left {
            flex: 1;
        }
        .bottom-bar-right {
            display: flex;
            gap: 10px;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(5px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="dark">
<div class="chatbox">
    <div class="top-bar">
        <h2>Chatbot GPT‑Neo SFT</h2>
        <div class="top-bar-buttons">
            <form method="POST" style="display:inline;">
                <input type="hidden" name="action" value="clear">
                <button type="submit">🧹 Limpiar conversación</button>
            </form>
            <button type="button" onclick="toggleTheme()">✨ Modo claro/oscuro</button>
        </div>
    </div>

    <div class="msg-container" id="msg-container">
        {% for u, b in history %}
            <div class="message user">
                <div class="bubble">
                    <div class="label">Tú</div>
                    {{ u }}
                </div>
            </div>
            <div class="message bot">
                <div class="bubble">
                    <div class="label">🤖 Asistente</div>
                    {{ b }}
                </div>
            </div>
        {% endfor %}
    </div>

    <form method="POST">
        <div class="bottom-bar">
            <div class="bottom-bar-left">
                <textarea name="msg" placeholder="Escribe tu pregunta aquí..."></textarea>
            </div>
            <div class="bottom-bar-right">
                <button type="submit">Enviar</button>
            </div>
        </div>
    </form>
</div>

<script>
    // Scroll automático hacia abajo
    var msgBox = document.getElementById('msg-container');
    msgBox.scrollTop = msgBox.scrollHeight;

    // Modo claro/oscuro dinámico
    function toggleTheme() {
        document.body.classList.toggle('light');
    }
</script>

</body>
</html>
"""

history = []

@app.route("/", methods=["GET", "POST"])
def index():
    global history
    if request.method == "POST":
        action = request.form.get("action", "").strip()
        if action == "clear":
            history = []
            return redirect(url_for("index"))
        user = request.form.get("msg", "").strip()
        if user:
            bot = generate_response(user)
            history.append((user, bot))
    return render_template_string(HTML, history=history)

app.run(debug=True)
