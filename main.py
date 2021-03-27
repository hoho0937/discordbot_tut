import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[', intents=intents)

client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">> bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(825240051817906176)
    await channel.send(F'{member} join!')
    print(F'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(825240084298858506)
    await channel.send(F'{member} join!')
    print(F'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency * 1000)}(ms)')

bot.run(jdata['TOKEN'])