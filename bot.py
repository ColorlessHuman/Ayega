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
