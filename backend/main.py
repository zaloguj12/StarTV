from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import random
import json
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="../frontend"), name="static") # attach the frontend folder

app.mount("/videos", StaticFiles(directory="videos"), name="videos") # attach the videos folder

with open("videos.json", "r", encoding="utf-8") as f:
    db = json.load(f)

@app.get("/")
def home():
    return FileResponse("../frontend/index.html")

@app.get("/video")
def watch():
    return random.choice(db["videos"])