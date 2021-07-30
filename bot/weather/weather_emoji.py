#!/usr/bin/env python3

def emojis() -> dict:
    WEATHER_EMOJIS = {
        "clouds": u'\U00002601',
        "storm": u'\U0001F329',
        "sun": u'\U00002600',
        "snow": u'\U00002744',
        "some_clouds": u'\U0001F324',
        "rain": u'\U0001F327'
    }

    assert type(WEATHER_EMOJIS) == dict, "No dict format"

    return WEATHER_EMOJIS
