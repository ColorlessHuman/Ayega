"""
Ayega
by Jyotirmoy Mandal

A Discord Bot
"""

import discord
import os
from discord.ext import commands


TOKEN = os.environ['AYEGA_TOKEN']

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('Apna Time Ayega!')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))

client.run(TOKEN)
