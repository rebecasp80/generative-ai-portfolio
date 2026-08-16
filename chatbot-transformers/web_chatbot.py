import gradio as gr
from chatbot_pipeline import generate_response

def chat(user_input, history):
    response = generate_response(user_input)
    history.append((user_input, response))
    return history, history

gr.ChatInterface(
    fn=chat,
    title="Chatbot GPT‑Neo SFT",
    description="Asistente profesional entrenado con SFT.",
).launch()
