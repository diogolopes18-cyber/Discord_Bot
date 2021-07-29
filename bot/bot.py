#!/usr/bin/env python3

__author__ = "Diogo Lopes"
__license__ = "MIT"
__email__ = "diogolopes18@ieee.org"

import os
import discord
import asyncio
from discord import colour
from dotenv import load_dotenv
from discord.ext import commands
import random
import wikipedia as wk
from pkgutil import iter_modules

from news import getNews
import colors as available_colors

modules = set(x[1] for x in iter_modules())
colors = available_colors.dict_colors()


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# Get the server name
GUILD = os.getenv('DISCORD_GUILD')
# Sets up bot prefix
bot = commands.Bot(command_prefix="!")
# Set Wikipedia language
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
        # Checks if the server name is the one we provided
        if(i.name == GUILD):
            break

    print(f'Connected to server {i.name}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel_send(f'Hi {member.name}! Welcome to IEEE ISEP Student Branch Discord')


@bot.command(pass_context=True)
async def info(ctx):

    server = ctx.guild
    #server_name = server.name
    # server_id = ctx.guild.id

    await ctx.send(f'Here is some info\nServer name: {server}')


@bot.command()
async def search(ctx, arg):
    """
    Searches the wikipedia for a specific topic
    """
    if(type(arg) != str):
        await ctx.send(f'Search terms must be a sentence')

    await ctx.send("Searching for results\n")
    await asyncio.sleep(1)

    # Wikipedia search result
    wiki_search = wk.summary(arg, sentences=1)
    await ctx.send(f'Here is the result: {wiki_search}')

# Always remember to add the () to the bot.command decorator


@bot.command()
async def channel_txt(ctx):
    """
    Creates new text channel upon command input
    """

    category_name = 'IEEE'
    # Fetches the category
    category = discord.utils.get(ctx.guild.categories, name=category_name)

    channel_names = ["chillout", "secret-room", "butterfly",
                     "willy wonka", "team-chat", "winnie the pooh"]

    # Choose the name randomly
    choice = random.choice(channel_names)
    await ctx.guild.create_text_channel(choice)


@bot.command()
async def bruh(ctx):
    await ctx.send("https://upload.wikimedia.org/wikipedia/en/b/b9/Terminator-2-judgement-day.jpg")


@bot.command()
async def britney(ctx):
    await ctx.send("https://pbs.twimg.com/media/Etaz6KGXIAA7Fok.jpg")


@bot.command()
@commands.has_role("Board")
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

        # Add new role inside server
        elif(arg1 == "role"):
            # Select color
            color = random.choice(colors)
            role_name = await ctx.guild.create_role(name=arg2, colour=color)
            await ctx.send(f'Role {role_name} has been created')

    except Exception as error:
        print("Bot error")


@bot.command()
@commands.has_role("Board")
async def edit(ctx, role, new_color):
    """
    Edit roles colours
    """

    assert new_color != "", "Need to specify a colour"

    # Check if color exists in the dict
    for i in colors:
        if(new_color == i):
            continue
        else:
            await ctx.send(f'{new_color} is not available')

    # Edit role
    await ctx.role.edit(name=role, colour=new_color)


######################
##  GET RECENT NEWS ##
######################
@bot.command()
async def news(ctx, cnt=None, topic_choice=None):
    """
    Retrieves recent news from the specified country
    """

    if(cnt == None):
        result = getNews(country="us")
    else:
        result = getNews(country=cnt)

            
    await ctx.send(f'```Here are the news:\n\n{result}```')

# Calls the web server so that the web server and the bot can be executed simultaneously
# server_thread()
bot.run(TOKEN)
