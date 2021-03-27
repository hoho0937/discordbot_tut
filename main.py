import discord
from discord.ext import commands
import json
import random

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
    channel = bot.get_channel(jdata['welcome_ch'])
    await channel.send(F'{member} join!')
    print(F'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(jdata['leave_ch'])
    await channel.send(F'{member} join!')
    print(F'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency * 1000)}(ms)')

@bot.command()
async def 本本抽獎(ctx):
    H_comic = random.choice(jdata['H_comics'])
    await ctx.send(F'抽到 {H_comic}')

@bot.command()
async def haachama(ctx):
    pic = discord.File('C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\pic\\haachama.jpg')
    await ctx.send(file = pic)

@bot.command()
async def 製粽(ctx):
    pic = discord.File('C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\pic\\th1.jpg')
    await ctx.send(file = pic)

bot.run(jdata['TOKEN'])