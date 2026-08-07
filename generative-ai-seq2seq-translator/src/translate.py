import torch
from src.config import DEVICE


def translate_sentence(model, sentence, de_vocab, en_vocab):
    model.eval()

    tokens = ["<SOS>"] + sentence.split() + ["<EOS>"]
    src = torch.tensor([de_vocab[t] for t in tokens]).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        hidden = model.encoder(src)
        input_token = torch.tensor([en_vocab["<SOS>"]]).to(DEVICE)
        output_sentence = []

        for _ in range(20):
            output, hidden = model.decoder(input_token, hidden)
            top1 = output.argmax(1).item()
            word = list(en_vocab.keys())[list(en_vocab.values()).index(top1)]

            if word == "<EOS>":
                break

            output_sentence.append(word)
            input_token = torch.tensor([top1]).to(DEVICE)

    return " ".join(output_sentence)
