#!/usr/bin/env python3

import os
import json
import requests
from dotenv import load_dotenv

# Env variables
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Global variables
url_request = "https://newsapi.org/v2/top-headlines"


class getNews():
    def __init__(self, country):
        self.relevance = "popularity"
        self.country = country
        self.key = API_KEY
        self.arr = []
        self.get_general_news()

    def get_general_news(self) -> list:

        params_request = {
            "country": self.country,
            "apiKey": self.key
        }

        result = requests.get(url_request, params=params_request).json()

        for titles in range(len(result["articles"])):
            news = result["articles"][titles]["title"]
            self.arr.append(news)

        return self.arr

    def __repr__(self) -> str:
        return repr(self.arr)
