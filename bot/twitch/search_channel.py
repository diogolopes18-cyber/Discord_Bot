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
        
    
    def is_channel_live(self) -> bool:
        '''
        Checks if the current channel is live
        '''

        request = self.channel_search()

        if(request["data"][0]["is_live"] == self.channel):
            return True
        else:
            return False
        
class StreamInformation(SearchChannel):
    def __init__(self, channel_name):
        super().__init__(channel_name)
    
    def get_stream_information(self):
        '''
        Returns information about the current stream
        Game name, streamer name and stream language
        '''

        if(self.channel_exists() == True and self.is_channel_live() == True):
            stream_info = {
                "streamer_name": self.channel_search()["data"][0]["broadcaster_login"],
                "stream_language": self.channel_search()["data"][0]["broadcaster_language"],
                "game_name": self.channel_search()["data"][0]["game_name"]
            }

            return stream_info
