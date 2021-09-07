#!/usr/bin/env python3

import os
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

