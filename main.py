import json
import random

with open("jokes.json") as f:
    data = json.load(f)

randomjoke = random.choice(data["jokes"])

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"msg": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/jokes")
def jokes():
    return data

@app.get("/jokes/random")
def jokes():
    return randomjoke
