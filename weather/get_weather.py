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
        test = self.weather_location()
        substr = emoji()

        print(substr)
        
        

obj = getCurrentWeather(location="Porto")
obj.associate_emoji_with_weather()