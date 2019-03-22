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
    print('Apna Time Ayega!')

# @client.event
# async def on_message(message):
#     author = message.author
#     content = message.content
#     print('{}: {}'.format(author, content))
#
# @client.event
# async def on_message_delete(message):
#     author = message.author
#     content = message.content
#     channel = message.channel
#     await client.send_message(channel, '{}: {}'.format(author, content))

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*kwargs):
    output = ''
    for word in kwargs:
        output += word
        output += ' '
    await client.say(output)


client.run(TOKEN)
