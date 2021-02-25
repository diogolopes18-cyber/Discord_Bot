#!/usr/bin/env python3

import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import random

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
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel_send(f'Hi {member.name}! Welcome to IEEE ISEP Student Branch Discord')

# @bot.event
# async def on_message(message,ctx):
#     bot_msg = message.content
#     guild = ctx.message.guild
    
#     ##################
#     ##Server Info
#     ##################   
#     # name = str(ctx.guild.name)
#     # description = str(ctx.guild.description)
#     # owner = str(ctx.guild.owner)
#     # server_id = str(ctx.guild.id)
    
#     #Check if the bot is sending himself messages
#     if(message.author == bot.user):
#         return
#     #Info command
#     elif(bot_msg.startswith('!info')):
#         await message.channel.send("Thanks for requesting info")
#     #Help command
#     elif(bot_msg.startswith('!help')):
#         await message.channel.send("how can I help?")
        

#Always remember to add the () to the bot.command decorator
@bot.command()
async def channel_txt(ctx):
    """
    Creates new text channel upon command input
    """
    
    category_name = 'IEEE'
    #Fetches the category
    category = discord.utils.get(ctx.guild.categories,name=category_name)
    
    channel_names = ["chillout", "secret-room", "butterfly", "willy wonka", "team-chat", "winnie the pooh"]
    
    #Choose the name randomly
    choice = random.choice(channel_names)
    await ctx.guild.create_text_channel(choice)
    
        
bot.run(TOKEN)