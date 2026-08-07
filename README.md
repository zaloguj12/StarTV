# StarTV
### StarTV is a project that lets users watch videos with no advertisements.

# Overview
### Backend --> Python with FastAPI
### Frontend --> HTML + CSS + JS
### Video Database --> JSON file with information about videos
### Video Storage/Serving --> FastAPI static file mounting

# File Architecture
```
StarTV/
|
├──backend/
|   ├──main.py          # FastAPI/Server
|   ├──videos.json      # Videos Database
|   └──videos/          # Local only
|       ├──1.mp4
|       ├──2.mp4
|       └──3.mp4
|
└──frontend/
    ├──images/
    ├──index.html
    ├──script.js
    └──style.css
```