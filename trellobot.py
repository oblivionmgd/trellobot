import sys, os, config
from datetime import datetime
from trello import TrelloClient
import discord
import asyncio
from discord.ext import commands

#tokens
tr_client = TrelloClient(
    config.tr_api_key,
    config.tr_api_secret,
    config.tr_token
)

dc_client = discord.Client()
config.ds_token

board_list = tr_client.list_boards()[7]
todo_list = board_list.list_lists()[0]
doing_list = board_list.list_lists()[2]
done_list = board_list.list_lists()[3]



#discord setup
bot = commands.Bot(command_prefix = '/')

@bot.event
async def on_ready():
    print('Hi Discord!')

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = '***Command Infomation***' , description = '使用可能なコマンドの一覧です。' , color = 0xc6ffdd)
    embed.add_field(name = '*/help*' , value = 'これだよ〜' , inline = False)
    embed.add_field(name = '*/ls 対象のリスト名*' , value = '指定したリスト内のカードを表示します。' , inline = False)
    embed.add_field(name = '*/shinchoku*' , value = '進捗を聞かれます。メンションが飛びまくるので注意。' , inline = False)
    embed.add_field(name = '*/move 移動したいカード名 移動先のリスト*' , value = 'カードを移動します。' , inline = False)
    embed.add_field(name = '*/comment 対象のカード名 コメント内容*' , value = 'コメントを入力できます。Markdownが使えます。多分。' , inline = False)

    await ctx.send(embed = embed)


@bot.command()
async def ls(ctx,aug1):
    if aug1 == "todo" or aug1 == "Todo":
        embed = discord.Embed(title = '***Todo List***' , description= '直近のタスクを表示します。着手したら **Doing** に移動してあげてください。\n[詳細を見る](https://trello.com/b/kICogz7C)', color = 0xfc466b)
        for card in todo_list.list_cards():
            embed.add_field(name = ':clipboard:' + card.name , value = '\u200b' , inline = True)

    if aug1 == "doing" or aug1 == "Doing":
        embed = discord.Embed(title = '***Doing List***' , description = '実行中のタスクを表示します。完了したら **Done** に移動させてあげてください。 \n[詳細を見る](https://trello.com/b/kICogz7C)', color = 0xfc466b)
        for card in doing_list.list_cards():
            embed.add_field(name = ':computer:' + card.name , value = '\u200b' , inline = True)

    if aug1 == "done" or aug1 == "Done":
       embed = discord.Embed(title = '***Doing List***' , description = '実行済みのタスクを表示します。お疲れ様でした!!\n[詳細を見る](https://trello.com/b/kICogz7C)',color = 0x3f5efb)
    for card in done_list.list_cards():
        embed.add_field(name = ':check:' + card.name , value = '\u200b' , inline = True)
    await ctx.send(embed = embed)


@bot.command()
async def shinchoku(ctx):
    await ctx.send('@everyone ***進 捗 ど う で す か***')

@bot.command()
async def move(ctx, aug1, aug2):
    for card in todo_list.list_cards():
        if card.name == aug1:
            if aug2 == 'Todo' or aug2 == 'todo':
                card.change_list(todo_list.id)
            elif aug2 == 'Doing' or aug2 == 'doing':
                card.change_list(doing_list.id)
            elif aug2 == 'Done' or aug2 == 'done':
                card.change_list(done_list.id)

    for card in doing_list.list_cards():
        if card.name == aug1:
            if aug2 == 'Todo' or aug2 == 'todo':
                card.change_list(todo_list.id)
            elif aug2 == 'Doing' or aug2 == 'doing':
                card.change_list(doing_list.id)
            elif aug2 == 'Done' or aug2 == 'done':
                card.change_list(done_list.id)

    for card in done_list.list_cards():
        if card.name == aug1:
            if aug2 == 'Todo' or aug2 == 'todo':
                card.change_list(todo_list.id)
            elif aug2 == 'Doing' or aug2 == 'doing':
                card.change_list(doing_list.id)
            elif aug2 == 'Done' or aug2 == 'done':
                card.change_list(done_list.id)


    await ctx.send('実行が終了しました。')

@bot.command()
async def comment(ctx, aug1, aug2):
    for card in todo_list.list_cards():
        if card.name == aug1:
            card.comment(datetime.now().strftime(aug2))

    for card in doing_list.list_cards():
        if card.name == aug1:
            card.comment(datetime.now().strftime(aug2))
    for card in done_list.list_cards():
        if card.name == aug1:
            card.comment(datetime.now().strftime(aug2))


    await ctx.send('実行が終了しました。')

bot.run(ds_token)
