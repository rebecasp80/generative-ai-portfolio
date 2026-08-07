import gradio as gr
import torch

from src.dataset import TranslationDataset
from src.models import Encoder, Decoder, Seq2Seq
from src.translate import translate_sentence
from src.config import DEVICE, DATA_DIR, MODEL_DIR


# -----------------------------
# Cargar dataset y vocabularios
# -----------------------------
dataset = TranslationDataset(DATA_DIR / "raw" / "de_en_samples.txt")
de_vocab = dataset.de_vocab
en_vocab = dataset.en_vocab

# -----------------------------
# Construir modelo Seq2Seq
# -----------------------------
encoder = Encoder(len(de_vocab))
decoder = Decoder(len(en_vocab))
model = Seq2Seq(encoder, decoder).to(DEVICE)

# -----------------------------
# Cargar pesos entrenados
# -----------------------------
model.load_state_dict(torch.load(MODEL_DIR / "best_model.pt", map_location=DEVICE))
print("Modelo cargado correctamente.")
model.eval()


# -----------------------------
# Función de traducción
# -----------------------------
def translate_fn(text):
    if not text.strip():
        return "Please enter a German sentence."
    return translate_sentence(model, text, de_vocab, en_vocab)


# -----------------------------
# Interfaz visual con Gradio
# -----------------------------
demo = gr.Interface(
    fn=translate_fn,
    inputs=gr.Textbox(lines=2, label="German sentence"),
    outputs=gr.Textbox(lines=2, label="English translation"),
    title="Seq2Seq Translator (German → English)",
    description="A simple RNN encoder–decoder translation model trained on a toy dataset."
)

if __name__ == "__main__":
    demo.launch()
