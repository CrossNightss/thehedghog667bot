import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
client = discord.Client()


@bot.event
async def on_ready():
    print("Le Bot est prêt")


@bot.event
async def on_message(message):
    
    if message.content.lower() == '$sonicx':
        await message.channel.send('https://www.dailymotion.com/playlist/x5szc2')
    
    if message.content.lower() == '!SonicXvd':
        await message.channel.send('https://www.twitch.tv/vinyleblood')

    if message.content.lower() == '!SonicXj':
        await message.channel.send('https://www.twitch.tv/vinyleblood')

    if message.content == 'salut':
        await message.channel.send(f'Salut {message.author} !')
    if message.content == 'Salut':
        await message.channel.send(f'Salut {message.author} !')
    if message.content == 'bye':
        await message.channel.send(f'A plus {message.author} ^^')
    if message.content == 'Bye':
        await message.channel.send(f'A plus {message.author} ^^')
        
    if message.content.endswith("quoi"):
        await message.channel.send('feur')
    if message.content.endswith("Quoi"):
        await message.channel.send('feur')
    await bot.process_commands(message)

@bot.command()
async def say(ctx, message=None):
    await ctx.send(message)




bot.run('OTM2MzY1OTkxMTYyNzA4MDA5.YfMIyQ.TE7fCCUokowXafRjRlshS99mvz0')
