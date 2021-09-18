#!/usr/bin/env python3

__author__ = "Diogo Lopes"
__license__ = "MIT"
__email__ = "diogolopes18@ieee.org"

import os
import discord
from discord.ext import commands
import asyncio

from dotenv import load_dotenv
import random
import wikipedia as wk
wiki_language = wk.set_lang("en")

from bot.news.news import getNews
import bot.colors.colors as available_colors
from bot.weather.get_weather import getCurrentWeather
from bot.crypto.crypto_exchange import CryptoValue

colors = available_colors.dict_colors()

#####################
##  ENV VARIABLES  ##
#####################
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("%s has connected to Discord!\n" % bot.user)

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
async def new(ctx, channel_type, name):

    if(channel_type == "" or name == ""):
        await ctx.send("Need to specify a command\n")

    try:
        if(channel_type == "voice"):
            await ctx.guild.create_voice_channel(name)
            await ctx.send(f'`Voice channel {name} has been created`')

        elif(channel_type == "text"):
            await ctx.guild.create_text_channel(name)
            await ctx.send(f'`Text channel {name} has been created`')

        elif(channel_type == "category"):
            await ctx.guild.create_category(name, overwrites=None, reason=None)
            await ctx.send(f'`{name} category has been created`')

        # Add new role inside server
        elif(channel_type == "role"):
            # Select color
            color = random.choice(colors)
            role_name = await ctx.guild.create_role(name=name, colour=color)
            await ctx.send(f'`Role {role_name} has been created`')

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
        result = getNews(country="pt")
    else:
        result = getNews(country=cnt)

    #Returns news about certain topic
    if(topic_choice != None):
        result = getNews().get_news_by_topic(topic=topic_choice)
        return ctx.send(f'Here are the news about {topic_choice}:\n\n{result}')

    format_result = "Here are the news\n\n>>> {}".format(result)
    await ctx.send(format_result)


@bot.command()
async def weather(ctx, place):
    """
    Retrieves weather from location
    """

    weather_result = getCurrentWeather(location=place)
    await ctx.send(f'Here it is\n{weather_result}')


@bot.command()
async def crypto(ctx, src=None, dest=None, amount=None):
    """
    Retrieves cryptocurrency information
    """

    if(src == None):
        result = CryptoValue()
        await ctx.send(f'The current cryptocurrency values are {result}')

    elif(src != None):
        assert amount > 0, "Can't accept negative numbers"
        conversion = CryptoValue().convert_crypto_currency(src=src, dest=dest, amount=amount)
        await ctx.send(f'Conversion result: {conversion}')


###############
##  SPOTIFY  ##
###############
# @bot.command()
# async def play(ctx, link=None):
#     """
#     Plays music from provided URL
#     """

#     import validators

#     assert validators.url(link) != False, "Not a valid URL"

#     command = MediaPlayer()




bot.run(TOKEN)