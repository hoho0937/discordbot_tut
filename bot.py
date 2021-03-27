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


for file_name in os.listdir('./cmds'):
    if file_name.endswith('.py'):
        bot.load_extension(F'cmds.{file_name[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])