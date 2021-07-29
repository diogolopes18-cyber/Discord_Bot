#!/usr/bin/env python3

import requests
import json
import os
from dotenv import load_dotenv
from weather_emoji import emojis as emoji

load_dotenv()
API_KEY = os.getenv('API_KEY')


class getCurrentWeather():
    _weather_results = []

    def __init__(self, location):
        self.key = API_KEY
        self.location = location
        self.base_url = "https://api.weatherbit.io/v2.0/current"
        
    
    def weather_location(self):

        request_params = {
            "key": self.key,
            "city": self.location
        }

        weather_request = requests.get(self.base_url, params=request_params).json()

        for i in range(len(weather_request["data"])):
            forecast = weather_request["data"][i]["weather"]["description"]
            self._weather_results.append(forecast)

        return self._weather_results

    def associate_emoji_with_weather(self):
        weather_list = self.weather_location()[0].lower()
        substr = emoji()
        
        #Looks for a correspondence between the returned weather and an emoji
        for key in substr.keys():
            split_string = weather_list.split()
            for word in split_string:
                if(word == key):
                    corresponding_emoji = substr[key]
        
        return corresponding_emoji