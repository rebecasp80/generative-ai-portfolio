from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.chat_engine import ChatEngine

app = FastAPI()

# Permitir acceso desde tu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar motor de chat
engine = ChatEngine(model_name="llama-3.1-8b-instant")

# Modelo de datos que recibe el frontend
class PromptRequest(BaseModel):
    prompt: str
    tone: str = "neutral"
    persona: str = "neutral"
    lang: str = "es"

# Endpoint principal
@app.post("/generate")
def generate_text(request: PromptRequest):
    response = engine.generate(
        prompt=request.prompt,
        persona=request.persona,
        tone=request.tone,
        lang=request.lang
    )
    return {"response": response}
