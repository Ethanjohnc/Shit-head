import os
import discord
import random


my_secret = os.environ['KEY']

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('~hello'):
    await message.channel.send('Hello there, I am Shit Head the slave of ethan')


















client.run(os.getenv('KEY'))