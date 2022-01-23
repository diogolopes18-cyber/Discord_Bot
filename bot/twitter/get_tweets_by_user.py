import requests
import os
from dotenv import load_dotenv

from bot.twitter.user_search import SearchUsername
from bot.twitter.urls import EndpointUrls

load_dotenv()
API_TOKEN = os.getenv("TOKEN")


class TweetsByUser:
    def __init__(self, username):
        self.token = API_TOKEN
        self.username = username

    def get_tweets_by_user(self):
        user_id = SearchUsername(username=self.username).get_user_id()
        url = EndpointUrls(endpoint="tweet_search", username=None, user_id=user_id).get_endpoint
        tweets = []

        headers = {
            "Authorization": f'Bearer {self.token}'
        }

        # Get the tweets for the user
        id_result = requests.get(url=url, headers=headers).json()

        for i in range(0, 10):
            tweets.append(id_result["data"][i]["id"])

        return tweets

    def get_tweets_by_id(self):
        tweets_ids = self.get_tweets_by_user()
        ids_list = list(map(int, tweets_ids))
        tweets_url = []

        for i in ids_list:
            tweets_url.append(
                EndpointUrls(endpoint="tweets_by_id", username=self.username, user_id=None, tweet_id=i).get_endpoint)

        return tweets_url
