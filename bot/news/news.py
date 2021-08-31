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
    def __init__(self, country, topic=None):
        self.relevance = "popularity"
        self.country = country
        self.topic = topic
        self.key = API_KEY
        self.arr = []

        if(self.topic != None):
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
    
    ######################
    ##  IN DEVELOPMENT  ##
    ######################
    def get_news_by_topic(self):

        params_request_topic = {
            "country": self.country,
            "apiKey": self.key,
            "topic": self.topic
        }

        result_topic = requests.get(url_request, params=params_request_topic).json()

        return result_topic

    def __repr__(self) -> str:
        return repr(self.arr)