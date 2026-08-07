from fastapi import FastAPI
import random
import json

app = FastAPI()

@app.get("/video")
def watch():
    return