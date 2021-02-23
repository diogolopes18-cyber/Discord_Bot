#!/usr/bin/env python3

import os
import discord
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Sets up client
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("Successfully connected to server")
    
client.run(TOKEN)