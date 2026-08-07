import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm import tqdm
import os

from src.config import DEVICE, DATA_DIR, MODEL_DIR
from src.dataset import TranslationDataset
from src.models import Encoder, Decoder, Seq2Seq


def train_model(model, dataset, epochs=50, lr=0.001):
    dataloader = DataLoader(dataset, batch_size=1, shuffle=True)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss(ignore_index=0)

    model.train()
    losses = []

    # Crear carpeta de checkpoints si no existe
    os.makedirs(MODEL_DIR / "checkpoints", exist_ok=True)

    for epoch in range(epochs):
        epoch_loss = 0

        print(f"\n🔵 Epoch {epoch+1}/{epochs}")

        for src, trg in tqdm(dataloader):
            src, trg = src.to(DEVICE), trg.to(DEVICE)

            optimizer.zero_grad()

            # Forward
            output = model(src, trg)

            # Alinear dimensiones para CrossEntropyLoss
            output_dim = output.shape[-1]
            output = output[:, 1:].reshape(-1, output_dim)
            trg = trg[:, 1:].reshape(-1)

            loss = criterion(output, trg)

            # Backprop
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()

        losses.append(epoch_loss)

        # Guardar checkpoint por época
        checkpoint_path = MODEL_DIR / "checkpoints" / f"seq2seq_epoch_{epoch+1}.pt"
        torch.save(model.state_dict(), checkpoint_path)
        print(f"💾 Checkpoint guardado: {checkpoint_path}")

    return model, losses


# ---------------------------------------------------------
# 🔥 BLOQUE PRINCIPAL — SE EJECUTA CON python -m src.train
# ---------------------------------------------------------

if __name__ == "__main__":
    print("📥 Cargando dataset...")
    dataset = TranslationDataset(DATA_DIR / "raw" / "de_en_samples.txt")

    print("⚙️ Construyendo modelo Seq2Seq...")
    encoder = Encoder(len(dataset.de_vocab))
    decoder = Decoder(len(dataset.en_vocab))
    model = Seq2Seq(encoder, decoder).to(DEVICE)

    print("🚀 Iniciando entrenamiento...")
    model, losses = train_model(model, dataset, epochs=50, lr=0.001)

    # Guardar mejor modelo (última época)
    best_model_path = MODEL_DIR / "best_model.pt"
    torch.save(model.state_dict(), best_model_path)

    print(f"\n🏁 Entrenamiento completado.")
    print(f"💾 Modelo final guardado en: {best_model_path}")
