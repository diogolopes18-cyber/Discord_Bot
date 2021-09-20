#!/usr/bin/env python3

import os
from dotenv import load_dotenv

from spotipy.oauth2 import SpotifyOAuth
from spotipy import util
import spotipy
from discord.utils import get
from discord import FFmpegPCMAudio


load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
user=os.getenv('username')
SECRET_CLIENT_ID=os.getenv('SECRET_CLIENT_ID')
redirect_uri='http://localhost:8888/callback/'



class MediaPlayer():
    def __init__(self):
        self.client_id_spotify = CLIENT_ID
        self.client_secret_id = SECRET_CLIENT_ID
        self.redirect_uri=redirect_uri
        self.scope="user-read-recently-played user-library-read user-read-playback-state,user-modify-playback-state"
        self.sp=None

        self.auth_manager=SpotifyOAuth(client_id=self.client_id_spotify, client_secret= self.client_secret_id, redirect_uri=self.redirect_uri)
        self.token_info=self.auth_manager.get_cached_token()

    def authorizationFlow(self):
        if(self.auth_manager.is_token_expired(self.token_info)):
            self.token_info = self.auth_manager.refresh_access_token(self.token_info['refresh_token'])
            token = self.token_info['access_token']
            self.sp = spotipy.Spotify(auth=token)

        self.sp=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id_spotify, client_secret= self.client_secret_id, redirect_uri=self.redirect_uri))



    def check_for_link(self):
        pass
        #Make connection to API
        #Check if URL exists
        #If it exists, check if it can play

    def track_name(self):
        
        pass
        '''
        Checks the track name and returns the track name when audio is active
        '''

    def bitrate_correction(self):
        pass
        '''
        Fixes the bitrate while playing to adjust to the OS's needs
        '''




