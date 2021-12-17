#!/usr/bin/env python3

import requests
import json
import os
from dotenv import load_dotenv

from bot.crypto.urls import url as url

load_dotenv()
API_KEY = os.getenv("KEY")

class CryptoValue():
    def __init__(self, currency=None):
        self.key = API_KEY
        self.currency = currency
        self.live_data_url = url("data")
        self.conversion_endpoint = url("conversion")
        self.crypto_values = []
        self.get_live_data()

    @staticmethod
    def curr_dict() -> tuple:
        curr = ("BTC", "ADA", "ETH", "DOGE")
        return curr

    def get_live_data(self):
        '''
        Returns the live rates of cryptocurrency
        '''

        currencies = self.curr_dict()

        #Returns main cryptocurrency data
        if(self.currency == None):

            request_params = {
                "access_key": self.key,
            }

            request = requests.get(self.live_data_url, params=request_params).json()

            #Returns the value for each one of the currencies
            for data in currencies:
                result = request["rates"][data]
                self.crypto_values.append(result)
            
            return self.crypto_values

            curr = {
                'BTC': None,
                'ADA': None,
                'ETH': None
            }

            request_params = {
                "access_key": self.key,
                "symbols": self.currency
            }

            curr_request = requests.get(self.live_data_url, params=request_params).json()

            for curr in curr_request:
                result = curr_request[curr]["rates"][self.currency]

            return result

    def convert_crypto_currency(self, src, dest, amount):
        '''
        Converts crypto currency into the desired coin
        '''

        available_coins = ["€", "$"]

        #Conversion
        conversion_parameters = {
            "access_key": self.key,
            "from": src,
            "to": dest,
            "amount": amount
        }

        conversion = requests.get(self.conversion_endpoint, params=conversion_parameters).json()

        for data in conversion:
            conversion_result = conversion[data]["result"]

        assert type(conversion_result) == int, "No available return"

        return conversion_result

    
    def __repr__(self):
        return str(self.crypto_values)