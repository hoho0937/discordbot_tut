import discord
from discord.ext import commands
import json
import random
import os


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
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'Loaded {extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'UnLoaded {extension}')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'ReLoaded {extension}')


for file_name in os.listdir('./cmds'):
    if file_name.endswith('.py'):
        bot.load_extension(F'cmds.{file_name[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])