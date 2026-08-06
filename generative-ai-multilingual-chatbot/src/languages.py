SUPPORTED_LANGUAGES = {
    "es": "Español",
    "en": "English",
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano"
}

def detect_language(text: str) -> str:
    # Simplificación: detección básica por caracteres
    if any(c in text for c in "ñáéíóú"):
        return "es"
    elif any(c in text for c in "àèìòù"):
        return "it"
    elif any(c in text for c in "äöüß"):
        return "de"
    elif any(c in text for c in "çéà"):
        return "fr"
    else:
        return "en"
