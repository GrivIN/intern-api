from fastapi import FastAPI

import os
import json

health_state = """
            {
        "status": "ok"
            }
               """

STATUS = json.loads(health_state)
CWD = os.getcwd()

JSON_JOKES_FILE_PATH = "%s/%s" % (CWD, "jokes.json")

JOKES_PROPERTIES = {}

with open(JSON_JOKES_FILE_PATH) as data_file:
    JOKES_PROPERTIES = json.load(data_file)

for joke in JOKES_PROPERTIES["jokes"]:
    print(joke["part1"], joke["part2"])

app = FastAPI()

@app.get("/")
async def index():
    return {"msg": "Hello World"}

@app.get("/health")
def health():
    return STATUS

@app.get("/jokes")
def jokes():
    return JOKES_PROPERTIES

from fastapi.testclient import TestClient

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == STATUS

def test_jokes():
    response = client.get("/jokes")
    assert response.status_code == 200
    assert response.json() == JOKES_PROPERTIES
