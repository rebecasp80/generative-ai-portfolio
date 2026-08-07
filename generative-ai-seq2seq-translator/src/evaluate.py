from nltk.translate.bleu_score import sentence_bleu

def calculate_bleu_score(hypothesis, references):
    return sentence_bleu([ref.split() for ref in references],
                         hypothesis.split())
