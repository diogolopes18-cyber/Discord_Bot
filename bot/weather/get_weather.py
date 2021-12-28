#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv
from bot.weather.weather_emoji import emojis as emoji

#####################
##  ENV VARIABLES  ##
#####################
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

        weather_request = requests.get(
            self.base_url, params=request_params).json()

        for i in range(len(weather_request["data"])):
            forecast = weather_request["data"][i]["weather"]["description"]
            self._weather_results.append(forecast)

        return self._weather_results

    def associate_emoji_with_weather(self):
        weather_list = self.weather_location()[0].lower()
        substr = emoji()

        # Looks for a correspondence between the returned weather and an emoji
        for key in weather_emojis.keys():
            if(weather_list.find(key) != -1):
                corresponding_emoji = weather_emojis[key]

        return f'The weather is gonna be {weather_list} {corresponding_emoji}'

class getForecast():
    def __init__(self, place, days=16):
        self.key = API_KEY
        self.place = place
        self.url = "https://api.weatherbit.io/v2.0/forecast"
        self.days = days
    
    def forecast(self):
    
        request_forecast_params = {
            "key": self.key,
            "city": self.place
        }

        if(self.days != 16):
            request_forecast_different_days = {
                "key": self.key,
                "city": self.place,
                "days": self.days
            }

            forecast_user_days = requests.get(self.url, params=request_forecast_different_days)

            return forecast_user_days
        
        else:
            forecast_default_days = requests.get(self.url, params=request_forecast_params)

            return forecast_default_days
        
        
