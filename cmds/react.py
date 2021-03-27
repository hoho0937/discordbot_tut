import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

dinner = ['炒飯','炒麵','屎','牛肉麵','牛排麵','雞排麵','水餃','咖哩飯','火鍋','鴨肉飯','羊肉燴飯','鍋燒意麵','羊肉米粉','麥當勞','KFC']
drink = ['奶茶','紅茶','綠茶','烏龍茶','青茶','豆漿','米漿','珍珠奶茶','咖啡','布丁奶茶','冬瓜茶','梅子綠茶','水','藍水','紅水']
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

    @commands.command()
    async def 要吃什麼(self,ctx):
        rand = random.randint(0, len(dinner))
        await ctx.send(F'{ctx.author} 根據大數據運算， 你今天可以吃 {dinner[rand]}')

    @commands.command()
    async def 要喝什麼(self,ctx):
        if '#3472' in str(ctx.author):
            await ctx.send(F'**{ctx.author}** 去喝 奶茶以外的')
        else:
            rand = random.randint(0, len(drink))
            await ctx.send(F'**{ctx.author}** 去喝  {drink[rand]}')

def setup(bot):
    bot.add_cog(React(bot))