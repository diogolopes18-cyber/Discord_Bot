#!/usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

# Env variables
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Global variables
url_request = "https://newsapi.org/v2/top-headlines"


class GetNews:
    def __init__(self, country, topic=None):
        self.relevance = "popularity"
        self.country = country
        self.key = API_KEY
        self.arr = []
        self.topic = topic

        if self.topic is not None:
            self.get_news_by_topic()
        else:
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

    def get_news_by_topic(self, topic):

        params_request_topic = {
            "country": self.country,
            "apiKey": self.key,
            "q": topic
        }

        result_topic = requests.get(url_request, params=params_request_topic).json()

        return result_topic

    def __repr__(self) -> str:
        return repr(self.arr)
