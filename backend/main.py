from fastapi import FastAPI
import random

app = FastAPI()

vid_1 = "videos/1.mp4"
vid_2 = "videos/2.mp4"
vid_3 = "videos/3.mp4"

videos = [vid_1, vid_2, vid_3]

@app.get("/videos/")
def watch():
    rand_num = random.randint(0, 2)
    print(videos[rand_num])
    return