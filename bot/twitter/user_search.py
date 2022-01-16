import os
import requests
from dotenv import load_dotenv

from bot.twitter.urls import EndpointUrls

load_dotenv()
API_TOKEN = os.getenv('TOKEN')


class UserNotFound(Exception):
    pass

class SearchUsername:
    def __init__(self, username):
        self.username = username
        self.api_token = API_TOKEN
        self.url = EndpointUrls(endpoint="search", username=self.username).get_endpoint()

    def get_twitter_name(self):
        headers = {
            "Authorization": f'Bearer {self.api_token}'
        }

        response = requests.get(url=self.url, headers=headers).json()

        return response["data"]["name"]