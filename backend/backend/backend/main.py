from fastapi import FastAPI
from pydantic import BaseModel

from ai.openai_client import ask_estud

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "app": "Estud",
        "status": "online"
    }

@app.post("/chat")
def chat(data: Question):

    answer = ask_estud(data.question)

    return {
        "answer": answer
    }
