import sys
import os
from datetime import datetime
from trello import TrelloClient
import discord
import asyncio

#tokens
tr_client = TrelloClient(
    api_key='5253ae83e899b0df3f779d5b6f47dbbf',
    api_secret='926354b8cf7a1acddac37acb89a4902fa48df51057ab817ab0acf4c2f389d5a0',
    token='f03236db68a8f95989d04d3a4173f8c3066610e6c885c0724ba98ab2b549eab0',
)

dc_client = discord.Client()
TOKEN = 'NjE2MTQwMzAwMDU3OTY4NjUx.XWZufQ.rVrST3vHScWYjmokVDkWn050kpE'

#trello
board = tr_client.list_boards()[7]
todo = board.list_lists()[0]
todo_option = board.list_lists()[1]
cards_todo = todo.list_cards()

#discord

#discord help
command_help = '/help:これです。\n\
    /todo:Todoリスト内のカードを表示します。\n\
    /doing:実行中のタスクを表示します。\n\
    /shinchoku:進捗を聞かれます。 '

@dc_client.event
async def on_ready():
    print('Hello Discord! xD')

@dc_client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/todo':
        await message.channel.send(cards_todo)

dc_client.run(TOKEN)
