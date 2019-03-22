"""
Ayega
by Jyotirmoy Mandal

A Discord Bot
"""

import discord
import logging
import os
from discord.ext import commands

# Log config
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


TOKEN = os.environ['AYEGA_TOKEN']

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Command Prefix = ?'))
    print('Apna Time Ayega!')

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


client.run(TOKEN)
