from fastapi import FastAPI
from src.services.queue.publisher import Publisher
import json

P = Publisher()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/usuario")
def salvar_usuario(mensagem: dict):
    print(mensagem)
    P.publish('meu_topico.aa', json.dumps(mensagem))
    return {"mensagem": "ok"}