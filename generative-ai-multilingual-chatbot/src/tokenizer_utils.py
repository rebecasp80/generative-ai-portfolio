class TokenizerUtils:
    def __init__(self):
        print("[TokenizerUtils] Groq models do not require local tokenizers.")

    def encode(self, text):
        return text

    def decode(self, text):
        return text
