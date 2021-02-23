#!/usr/bin/env python3

import os
import discord
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Get the server name
GUILD = os.getenv('DISCORD_GUILD')

#Sets up client
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!\n')
    
    for i in client.guilds:
        #Checks if the server name is the one we provided
        if(i.name == GUILD):
            break
    
    print(f'Connected to server {i.name}')
    
client.run(TOKEN)