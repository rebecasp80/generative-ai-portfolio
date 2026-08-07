import torch
from torch.utils.data import Dataset
from src.vocab import build_vocab, encode_sentence


class TranslationDataset(Dataset):
    def __init__(self, path):
        self.pairs = []

        # Leer archivo línea por línea
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                # Saltar líneas vacías
                if not line:
                    continue

                # Dividir por espacios (formato flexible)
                parts = line.split()

                # Si no hay suficientes palabras, saltar
                if len(parts) < 2:
                    continue

                # Dividir la línea en dos mitades: alemán ↔ inglés
                mid = len(parts) // 2
                de = " ".join(parts[:mid])
                en = " ".join(parts[mid:])

                self.pairs.append((de, en))

        # Construir vocabularios alemán e inglés
        self.de_vocab, self.en_vocab = build_vocab(self.pairs)

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, idx):
        de, en = self.pairs[idx]

        # Convertir frases a tensores
        src = torch.tensor(encode_sentence(de, self.de_vocab))
        trg = torch.tensor(encode_sentence(en, self.en_vocab))

        return src, trg
