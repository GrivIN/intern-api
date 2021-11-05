import json
import random

JOKES_LIBRARY = json.load(open("jokes.json"))


for joke in JOKES_LIBRARY["jokes"]:
    allthejokes = joke

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
    return JOKES_LIBRARY

@app.get("/jokes/random")
def jokes():
    return randomjoke
