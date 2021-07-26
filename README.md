# IEEE_ISEP_Discord_Bot

IEEE ISEP Student Branch Discord server bot for automating some processes like creating channels, roles or just getting information

![](https://travis-ci.com/diogolopes18-cyber/IEEE_ISEP_Discord_Bot.svg?branch=main)
![](https://img.shields.io/github/languages/count/diogolopes18-cyber/IEEE_ISEP_Discord_Bot)
![](https://img.shields.io/github/repo-size/diogolopes18-cyber/IEEE_ISEP_Discord_Bot)
![](https://img.shields.io/github/license/diogolopes18-cyber/IEEE_ISEP_Discord_Bot)

# Installation

First of all, you need to have `pip3` installed in your local machine. To do so, run:

`sudo apt-get update`

`sudo apt-get -y install python3-pip`

To check if `pip3` was successfully installed, type:

`pip3 --version`

# Usage

**1. Running bot**

- ```cd bot```
- ```python3 bot.py```

**2. Basic Commands**

- ```!info``` returns information about the server like its owner and numbr of members
- ```!new <channel_type> <channel_name>``` creates a text or voice channel depending on the second argument value
- ```!search <question>``` searches for a specific topic and returns the answer from Wikipedia
- ```!news``` returns the top news of the day from a specified country
- ```!channel_txt``` creates a text channel with a random name

**3. Upcoming features**

- **Twitch integration** in order for a user to get information about a specific streamer in their DMs
- **Moderation measures** such as spam control
- **Spotify suggestions**, users get the top Spotify playlist suggestions for a specific music genre

# Contributing

Pull requests are welcome. Please open a issue first to discuss the changes, and then open a pull request.
