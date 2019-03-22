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

client.run(TOKEN)
