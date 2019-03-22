"""
Ayega
by Jyotirmoy Mandal

A Discord Bot
"""

import discord
from discord.ext import commands
import logging
import os
import youtube_dl

# Log config
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


TOKEN = os.environ['AYEGA_TOKEN']

client = commands.Bot(command_prefix='?')
# Remove default help command
client.remove_command('help')

players = { }


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Half Life 3'))
    print('Apna Time Ayega!')


@client.command()
async def ping():
    await client.say('Pong!')


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        color=discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='?ping', value='Displays Pong!', inline=False)
    embed.add_field(name='?help', value='Displays this message', inline=False)

    await client.send_message(author, embed=embed)


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


client.run(TOKEN)
