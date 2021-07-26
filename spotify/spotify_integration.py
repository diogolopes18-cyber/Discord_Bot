#!/usr/bin/env python3

import requests
import json
from dotenv import load_dotenv

load_dotenv()
SPOTIFY_API_KEY = os.getenv('SPOTIFY_API_KEY')

class spotifyReleases():
    
    api_key = SPOTIFY_API_KEY

    def __init__(self, query):
        self.query = query
        self.url = "https://api.spotify.com/v1/search"
    
    def authorization_header(self):

        header = {
            "Authorization": f'Bearer {self.api_key}'
        }
    
    def search_artist_no_type(self):

        request_params = {
            "q": self.query
        }

        get_request = requests.get(self.url, headers=self.authorization_header(), params=request_params).json()

        return get_request
    
    def search_artist_by_type(self, type):

        self.type = type

        request_params_type = {
            "q": self.query,
            "type": self.type
        }

        get_request_type = requests.get(self.url, headers=self.authorization_header(), params=request_params_type).json()

        return get_request_type