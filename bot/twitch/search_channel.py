import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CLIENT_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")
URL = os.getenv("API_URL")

class SearchChannel:
    def __init__(self, channel_name):
        self.key = API_KEY
        self.client_id = CLIENT_ID
        self.url = URL
        self.channel = channel_name

    def build_params(self):
        params = {
            "query": self.channel
        }

        return params

    def build_header(self):
        headers = {
            "Authorization": self.key,
            "Client-Id": self.client_id
        }

        return headers

    def channel_search(self) -> bool:
        '''
        Searches for channels that match the specified name
        '''

        request = requests.get(self.url,
                               params=self.build_params(),
                               auth=self.build_header()).json()
        
        return request

    def channel_exists(self):

        request = self.channel_search()

        if(request["data"][0]["broadcaster_login"] == self.channel):
            return True
        else:
            return False
