import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 本本抽獎(self,ctx):
        rand = random.randint(10000,30000)
        H_comic = random.choice(jdata['H_comics'])
        await ctx.send(F'抽到 {rand}')

    @commands.command()
    async def haachama(self,ctx):
        pic = discord.File('C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\pic\\haachama.jpg')
        await ctx.send(file=pic)

    @commands.command()
    async def 製粽(self,ctx):
        pic = discord.File('C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\pic\\th1.jpg')
        await ctx.send(file=pic)

    @commands.command()
    async def 肉便器(self,ctx):
        pic = discord.File('C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\pic\\EMT.jpg')
        await ctx.send(file=pic)

    @commands.command()
    async def TSJ(self,ctx):
        pic = discord.File('C:\\Users\\eric5\\PycharmProjects\\discordbot_tut\\pic\\TSJ.jpg')
        await ctx.send(file=pic)

def setup(bot):
    bot.add_cog(React(bot))