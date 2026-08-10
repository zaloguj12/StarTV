from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import random
import json
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
VIDEOS_DIR = os.path.join(BASE_DIR, "videos")
VIDEOS_JSON = os.path.join(BASE_DIR, "videos.json")

app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend") # attach the frontend folder

app.mount("/videos", StaticFiles(directory=VIDEOS_DIR), name="videos") # attach the videos folder

with open(VIDEOS_JSON, "r", encoding="utf-8") as f:
    db = json.load(f)

@app.get("/")
def home():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/video")
def watch():
    return random.choice(db["videos"])