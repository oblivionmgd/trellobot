import discord
import asyncio

client = discord.Client()
TOKEN = 'NjE2MTQwMzAwMDU3OTY4NjUx.XWZufQ.rVrST3vHScWYjmokVDkWn050kpE'

@client.event
async def on_ready():
    print('にゃーん')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/hi':
        await message.channel.send('Hi')

client.run(TOKEN)
