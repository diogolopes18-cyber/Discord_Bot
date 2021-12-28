#!/usr/bin/env python3

def url(endpoint) -> str:

    if(endpoint == "data"):
        return "http://api.coinlayer.com/live"

    elif(endpoint == "conversion"):
        return "http://api.coinlayer.com/convert"
