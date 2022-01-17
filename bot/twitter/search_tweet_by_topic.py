import os

import requests
from dotenv import load_dotenv

from bot.twitter.urls import EndpointUrls

load_dotenv()
API_TOKEN = os.getenv('TOKEN')


class TweetByTopic:
    def __init__(self, topic):
        self.token = API_TOKEN
        self.topic = topic
        self.url = EndpointUrls(endpoint="tweet_by_topic", username=None).get_endpoint

    def get_recent_tweets_by_topic(self):
        headers = {
            "Authorization": f'Bearer {self.token}'
        }

        params = {
            "query": self.topic
        }

        return requests.get(self.url, headers=headers, params=params).json()

    def organize_tweets(self):
        tweets = self.get_recent_tweets_by_topic()
        tweets_content = []

        for i in range(0,10):
            tweets_content.append(tweets["data"][i]["text"])

        return tweets_content
