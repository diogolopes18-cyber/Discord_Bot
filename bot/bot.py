#!/usr/bin/env python3

import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import random
import wikipedia as wk
from pkgutil import iter_modules

modules = set(x[1] for x in iter_modules())


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Get the server name
GUILD = os.getenv('DISCORD_GUILD')

#Sets up bot prefix
bot = commands.Bot(command_prefix="!")

#Set Wikipedia language
wiki_language = wk.set_lang("en")


def check_for_modules():
    with open('requirements.txt', 'rb') as f:
        for line in f:
            requirement = line.rstrip()
            if not requirement in modules:
                os.system("pip3 install -r requeriments.txt")

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

@bot.command()
async def info(ctx):
    
    server = ctx.message.author.server
    server_name = server.name
    server_id = server.id
    server_owner = server.owner.name

    print("server name: {}"
          "server id: {}"
          "server owner: {}"
          .format(server_name, server_id, server_owner))
    
@bot.command()
async def search(ctx,arg):
    """
    Searches the wikipedia for a specific topic
    """
    if(type(arg) != str):
        exit(-1)
        
    await ctx.send("Searching for results\n")
    await asyncio.sleep(1)
    
    #Wikipedia search result
    wiki_search = wk.summary(arg,sentences=1)
    await ctx.send(f'Here is the result: {wiki_search}')

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

@bot.command()
async def bruh(ctx):
    await ctx.send("https://upload.wikimedia.org/wikipedia/en/b/b9/Terminator-2-judgement-day.jpg")

@bot.command()
async def britney(ctx):
    await ctx.send("https://pbs.twimg.com/media/Etaz6KGXIAA7Fok.jpg")
    
@bot.command()
async def new(ctx, arg1, arg2):
    if(arg1 == "" or arg2 == ""):
        await ctx.send("Need to specify a command\n")
    try:
        if(arg1 == "voice"):
            await ctx.guild.create_voice_channel(arg2)
        elif(arg1 == "text"):
            await ctx.guild.create_text_channel(arg2)
        elif(arg1 == "category"):
            await ctx.guild.create_category(arg2, overwrites=None, reason=None)
        #Add new role inside server
        elif(arg1 == "role"):
            await ctx.guild.create_role(name=arg2)
            
    except Exception as error:
        print("Bot error")
    
        
bot.run(TOKEN)