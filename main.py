from fastapi import FastAPI
from Scraper import Scraper
from MultiScraper import MultiScraper
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

news = Scraper()
multiNews = MultiScraper()

@app.get("/{endPoint}")
async def printNews(endPoint):
    return news.findNews(endPoint)

@app.get("/{endPoint}/{page}")
async def printMultipleNews(endPoint ,page):
    return multiNews.findNews(endPoint,page)