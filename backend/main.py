from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import random
import json

app = FastAPI()

app.mount("/videos", StaticFiles(directory="videos"), name="videos") # attach the videos folder

with open("videos.json", "r", encoding="utf-8") as f:
    db = json.load(f)

@app.get("/video")
def watch():
    return random.choice(db["videos"])