#!/usr/bin/env python3

import os
import requests
import json
from dotenv import load_dotenv

import spotify

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID_SPOTIFY')


class authorizationFlow():
    def __init__(self):
        self.client_id_spotify = CLIENT_ID

    def pkce_authorization(self):
        return -1

class MediaPlayer():
    def __init__(self):
        self.client_id = CLIENT_ID
        self.session = spotify.Session()

    def check_for_link(self, playlist_url):
        #Make connection to API
        #Check if URL exists
        #If it exists, check if it can play

    def track_name(self):
        '''
        Checks the track name and returns the track name when audio is active
        '''

    def bitrate_correction(self):
        '''
        Fixes the bitrate while playing to adjust to the OS's needs
        '''

class spotifyReleases():

    api_key = SPOTIFY_API_KEY

    def __init__(self, query):
        self.query = query
        self.url = "https://api.spotify.com/v1/search"

    def authorization_header(self):

        header = {
            "Authorization": f'Bearer {self.api_key}'
        }

        return header

    def search_artist_no_type(self):

        request_params = {
            "q": self.query
        }

        get_request = requests.get(
            self.url, headers=self.authorization_header(), params=request_params).json()

        return get_request

    def search_artist_by_type(self, type):

        self.type = type

        request_params_type = {
            "q": self.query,
            "type": self.type
        }

        get_request_type = requests.get(
            self.url, headers=self.authorization_header(), params=request_params_type).json()

        return get_request_type
