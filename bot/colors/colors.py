#!/usr/bin/env

import discord
from discord import colour


def dict_colors() -> dict:

    # Color dictionary
    dictOfColors = {'1': discord.Color.default(),
                    '2': discord.Color.teal(),
                    '3': discord.Color.dark_teal(),
                    '4': discord.Color.green(),
                    '5': discord.Color.dark_green(),
                    '6': discord.Color.blue(),
                    '7': discord.Color.purple(),
                    '8': discord.Color.dark_purple(),
                    '9': discord.Color.magenta(),
                    '10': discord.Color.dark_magenta(),
                    '11': discord.Color.gold(),
                    '12': discord.Color.dark_gold(),
                    '13': discord.Color.orange(),
                    '14': discord.Color.dark_orange(),
                    '15': discord.Color.red(),
                    '16': discord.Color.dark_red()
                    }

    return dictOfColors
