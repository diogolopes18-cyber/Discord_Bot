from bot.twitter.user_search import SearchUsername
from bot.twitter.search_tweet_by_topic import TweetByTopic
from bot.twitter.get_tweets_by_user import TweetsByUser
from bot.crypto.crypto_exchange import CryptoValue
from bot.weather.get_weather import CurrentWeather
import bot.colors.colors as available_colors
from bot.news.news import GetNews
from bot.translation.translate_sentence import Translate
from bot.job_search.search_job_by_country import SearchJobs

import os
import discord
from discord.ext import commands
import asyncio

from dotenv import load_dotenv
import random
import wikipedia as wk

wiki_language = wk.set_lang("en")

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
        if (i.name == GUILD):
            break

    print(f'Connected to server {i.name}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel_send(f'Hi {member.name}! Welcome to IEEE ISEP Student Branch Discord')


@bot.command(pass_context=True)
async def info(ctx):
    server = ctx.guild
    # server_name = server.name
    # server_id = ctx.guild.id

    await ctx.send(f'Here is some info\nServer name: {server}')


@bot.command()
async def search(ctx, arg):
    """
    Searches the wikipedia for a specific topic
    """
    if (type(arg) != str):
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
    if (channel_type == "" or name == ""):
        await ctx.send("Need to specify a command\n")

    try:
        if (channel_type == "voice"):
            await ctx.guild.create_voice_channel(name)
            await ctx.send(f'`Voice channel {name} has been created`')

        elif (channel_type == "text"):
            await ctx.guild.create_text_channel(name)
            await ctx.send(f'`Text channel {name} has been created`')

        elif (channel_type == "category"):
            await ctx.guild.create_category(name, overwrites=None, reason=None)
            await ctx.send(f'`{name} category has been created`')

        # Add new role inside server
        elif (channel_type == "role"):
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
        if (new_color == i):
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

    if (cnt == None):
        result = GetNews(country="pt")
    else:
        result = GetNews(country=cnt)

    # Returns news about certain topic
    if (topic_choice != None):
        result = GetNews().get_news_by_topic(topic=topic_choice)
        return ctx.send(f'Here are the news about {topic_choice}:\n\n{result}')

    format_result = "Here are the news\n\n>>> {}".format(result)
    await ctx.send(format_result)


########################
##  WEATHER COMMANDS  ##
########################

@bot.command()
async def weather(ctx, place):
    """
    Retrieves weather from location
    """

    weather_result = CurrentWeather(
        location=place).associate_emoji_with_weather()
    await ctx.send(f'Weather for {place}\n{weather_result}')


#######################
##  CRYPTO COMMANDS  ##
#######################

@bot.command()
async def crypto(ctx, custom_curr=None):
    """
    Retrieves cryptocurrency information
    """

    if (custom_curr == None):
        result = CryptoValue().get_live_data
        format_result = "The current cryptocurrency values are\n>>> {}".format(
            result)
        await ctx.send(format_result)

    elif (custom_curr):
        result = CryptoValue(currency=custom_curr).get_live_data
        format_result = f'The current cryptocurrency value is\n>>> {result} $'
        await ctx.send(format_result)


########################
##  TWITTER COMMANDS  ##
########################

@bot.command()
async def twitter_username(ctx, username):
    """
    Retrieves information about a stream
    If the stream is live, what game is being played, the stream language
    """

    result = SearchUsername(username=username).get_twitter_name()
    await ctx.send(f'Here is the Twitter name of the username {username}:\n> {result}')


@bot.command()
async def tweets_topic(ctx, topic):
    """
    Retrieves the latest tweets for the requested topic
    """

    result = TweetByTopic(topic=topic).organize_tweets()

    for i in result:
        format_result = "\n>>> {}".format(i)
        await ctx.send(format_result)


@bot.command()
async def tweets_user(ctx, username):
    """
    Returns the last tweets for a specified user
    """

    result = TweetsByUser(username=username).get_tweets_by_id()

    for tweet in result:
        format_result = "\n>>> {}".format(tweet)
        await ctx.send(format_result)


##########################
##  TRANSLATE COMMANDS  ##
##########################

@bot.command()
async def translate(ctx, sentence, dest_lang):
    translate_sentence = Translate(dest_lang,sentence).translate_sentence
    await ctx.send("\n> {}".format(translate_sentence))


##########################
##  JOB SEARCH COMMANDS ##
##########################

@bot.command()
async def jobs(ctx, country=None, role=None):
    jobs = SearchJobs(country, role).format_job_search()

    format_result = "\n>>> {}".format(jobs)
    await ctx.send(format_result)

bot.run(TOKEN)
