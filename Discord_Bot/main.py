import discord  # Подключаем библиотеку
from discord.ext import commands

intents = discord.Intents.default()  # Подключаем "Разрешения"
intents.message_content = True

# Задаём префикс и токен
config = {
    'token': 'MTA1NDgzMDk5OTk4NjUyMDEwNg.Gzsjli.O33hW0y7T6TLUHILV9HcAABGPUNQH1jSIpEYx4',
    'prefix': '`',
}

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.event
async def on_ready():
    print('Бот запущен')

# Пишим в чатей (`ping), и бот выдаст сообщение -> (pong)
@bot.command()
async def ping(ctx):
    print(ctx)
    await ctx.send('pong')

# Пишим в чатей (`hi), и бот выдаст своё особое приветствие
@bot.command()
async def hi(ctx):
    await ctx.send('Привет я Консерва! Если я чем то могу помочь подскажи мне!')

# Пишим в чатей (`say ), затем пробел и ОБЯЗАТЕЛЬНО после пробела что нибудь)) Этот "что-то" бот и повторит!
# Например, на запись в чате(без скобок) - (`say hello), бот ответи -> hello
# Например, на запись в чате(без скобок) - (`say "hello world"), бот ответи -> hello world
# Например, на запись в чате(без скобок) - (`say hello world), бот ответи -> hello
@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)

# Комманда для суммирования.
# Пишем в чате префикс (`), потом без пробела слово sum, затем пробел 1-ое число, после пробел и 2-ое число
# Работает только с целыми числами (int) !!!
# Например, на запись в чате(без скобок) - (`sum 3 5), бот ответи "8"
@bot.command()
async def sum(ctx, a: int, b: int):
    await ctx.send(a + b)

# Функция эхо
# @bot.event
# async def on_message(ctx):
#     if ctx.author != bot.user:
#         await ctx.reply(ctx.content)
        
#         print()

bot.run(config['token'])


# config = {
#     'token': 'your-token',
#     'prefix': 'prefix',
# }

# bot = commands.Bot(command_prefix=config['prefix'])


# @bot.event
# async def on_message(ctx):
#     if ctx.author != bot.user:
#         await ctx.reply(ctx.content)

# bot.run(config['token'])
