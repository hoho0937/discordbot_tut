import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Loaded(Cog_Extension):
    @commands.command()
    async def load(self,ctx, extension):
        self.bot.load_extension(F'cmds.{extension}')
        await ctx.send(F'Loaded {extension}')

    @commands.command()
    async def unload(self,ctx, extension):
        self.bot.unload_extension(F'cmds.{extension}')
        await ctx.send(F'UnLoaded {extension}')

    @commands.command()
    async def reload(self,ctx, extension):
        self.bot.reload_extension(F'cmds.{extension}')
        await ctx.send(F'ReLoaded {extension}')

def setup(bot):
    bot.add_cog(Loaded(bot))