#!/usr/bin/env python3

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

class twitchFetchStream():
    
    """
    Checks if a stream is valid or if the streamer exists
    """
    def __init__(self, streamer):
        self.apikey = API_KEY


class embbedStream(twitchFetchStream):
    
    if(twitchFetchStream == True):
        pass

