import json

with open('jokes.json', 'r') as myfile:
    data=myfile.read()

JOKES_LIBRARY_JSON = json.loads(data)

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
    return JOKES_LIBRARY_JSON

@app.get("/jokes/random")
def jokes():
    return 
