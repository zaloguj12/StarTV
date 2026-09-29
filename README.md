# [StarTV](https://star-tv-ten.vercel.app/)
### StarTV is a project that lets users watch videos with no advertisements.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3a6496d7-a8a0-499c-8ed3-12e29b66fb55" />

# Overview
### Backend --> Python with FastAPI
### Frontend --> HTML + CSS + JS
### Video Database --> JSON file with information about videos
### Video Storage/Serving --> FastAPI static file mounting from an R2 Bucket dev link (dont have a domain lol)

# File Architecture
```
StarTV/
|
├──videos.json      # Videos Database
|
├──api/
|   └──main.py      # FastAPI/Server
|
└──frontend/
    ├──images and icons
    ├──index.html
    ├──script.js
    └──style.css
```

# Deployment

Deployed with Vercel at [(SITE)](https://star-tv-ten.vercel.app/) with an R2 bucket from CloudFlare as video storage.

# Info

This project is for [Stardance](https://stardance.hackclub.com/), it's a YSWS program from Hackclub a non-profit that encourages teens to try out new things with technology.
