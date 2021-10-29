from fastapi import FastAPI

import os
import json

CWD = os.getcwd()

JSON_JOKES_FILE_PATH = "%s/%s" % (CWD, "jokes.json")

JOKES_PROPERTIES = {}

with open(JSON_JOKES_FILE_PATH) as data_file:
    JOKES_PROPERTIES = json.load(data_file)

for joke in JOKES_PROPERTIES["jokes"]:
    print(joke["part1"], joke["part2"])

app = FastAPI()

@app.get("/")
def index():
    return "Welcome"

@app.get("/health")
def healthpoint():
    return "the localhost is in a Healthy state"

@app.get("/jokes")
def jokes():
    return JOKES_PROPERTIES
