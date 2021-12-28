#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv
from bot.crypto.urls import url as url

load_dotenv()
API_KEY = os.getenv("KEY")


class CryptoValue:
    def __init__(self, currency=None):
        self.key = API_KEY
        self.currency = currency
        self.live_data_url = url("data")
        self.conversion_endpoint = url("conversion")

    def request_all_coins(self):
        request_params = {
            "access_key": self.key,
        }

        request = requests.get(
            self.live_data_url, params=request_params).json()

        return request

    def request_specific_coin(self):
        request_params = {
            "access_key": self.key,
            "symbols": self.currency
        }

        curr_request = requests.get(
            self.live_data_url, params=request_params).json()

        return curr_request

    def get_live_data(self):
        '''
        Returns the live rates of cryptocurrency
        '''

        request = self.request_all_coins()
        crypto_values = list()
        curr = {
            "BTC": 0,
            "ADA": 0,
            "ETH": 0,
            "DOGE": 0
        }

        # Returns main cryptocurrency data
        if(self.currency == None):

            # Returns the value for each one of the currencies
            for data in curr.keys():
                result = request["rates"][data]
                crypto_values.append(result)

            for i in curr.keys():
                for val in crypto_values:
                    curr[i] = val

            return curr

        else:

            curr_request = self.request_specific_coin()
            for curr in curr_request:
                result = curr_request[curr]["rates"][self.currency]

            return result

    def convert_crypto_currency(self, src, dest, amount):
        '''
        Converts crypto currency into the desired coin
        '''

        # Conversion
        conversion_parameters = {
            "access_key": self.key,
            "from": src,
            "to": dest,
            "amount": amount
        }

        conversion = requests.get(
            self.conversion_endpoint, params=conversion_parameters).json()

        for data in conversion:
            conversion_result = conversion[data]["result"]

        return conversion_result
