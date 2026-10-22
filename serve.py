import requests
from fastapi import FastAPI
from pydantic import BaseModel


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen2.5:1.5b"

app = FastAPI()


class GenerateRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 256


@app.post("/generate")
def generate(req: GenerateRequest):
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "messages": [{"role": "user", "content": req.prompt}],
            "stream": False,
            "options": {"num_predict": req.max_new_tokens},
        },
        timeout=600,
    )
    r.raise_for_status()
    return {"response": r.json()["message"]["content"]}
















