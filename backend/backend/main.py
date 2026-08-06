from fastapi import FastAPI

app = FastAPI(
    title="Estud AI",
    description="A IA que ensina, não apenas responde.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "app": "Estud AI",
        "version": "1.0.0",
        "status": "online",
        "message": "Bem-vindo ao Estud!"
    } 
