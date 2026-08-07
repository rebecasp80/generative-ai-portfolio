from collections import Counter

SPECIAL_TOKENS = ["<PAD>", "<SOS>", "<EOS>"]


def build_vocab(pairs):
    de_words = []
    en_words = []

    for de, en in pairs:
        de_words.extend(de.split())
        en_words.extend(en.split())

    de_vocab = {tok: i for i, tok in enumerate(SPECIAL_TOKENS)}
    en_vocab = {tok: i for i, tok in enumerate(SPECIAL_TOKENS)}

    for word in Counter(de_words):
        de_vocab[word] = len(de_vocab)

    for word in Counter(en_words):
        en_vocab[word] = len(en_vocab)

    return de_vocab, en_vocab


def encode_sentence(sentence, vocab):
    tokens = ["<SOS>"] + sentence.split() + ["<EOS>"]
    return [vocab[t] for t in tokens]
