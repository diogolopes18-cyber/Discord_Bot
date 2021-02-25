#!/usr/bin/env python3

import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Get the server name
GUILD = os.getenv('DISCORD_GUILD')

#Sets up bot prefix
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!\n')
    
    for i in bot.guilds:
        #Checks if the server name is the one we provided
        if(i.name == GUILD):
            break
    
    print(f'Connected to server {i.name}')

@bot.event
async def on_message(message,ctx):
    bot_msg = message.content
    
    ##################
    ##Server Info
    ##################   
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    server_id = str(ctx.guild.id)
    
    #Check if the bot is sending himself messages
    if(message.author == bot.user):
        return
    #Info command
    elif(bot_msg.startswith('!info')):
        await message.channel.send("Server name: %s\nDescription: %s\nOwner: %s\nID: %s" % (name,description,owner,server_id))
    #Help command
    elif(bot_msg.startswith('!help')):
        await message.channel.send("How can I help?")

@bot.command
async def ServerInfo(ctx):
    """
    Return information about the server if requested by the user
    """
    
    server = ctx.guild
    server_name = guild.name
    server_creation_date = server.created_at
    owner_server = server.owner.name
    
    return server, server_name, server_creation_date, owner_server
        
bot.run(TOKEN)