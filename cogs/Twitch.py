'''
Twitch.py

A cog file to hold functions for the Twitch events of the Colby Gaming Server
'''
import discord
from discord.ext import commands


class Twitch(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('\t- Twitch has loaded')

    @commands.command(name="hello")
    async def hello(self, ctx):
        user = str(ctx.message.author)

        await ctx.send(f"Hi {user[:-5]}")

    @commands.command(name="tlive")
    async def live(self, ctx, twitchname, streamer: discord.Member = None):
        # tell the invoker if they didn't mention someone, then quit out w/out throwing an exception
        if streamer is None:
            await ctx.send(f'{ctx.message.author.mention}, please make sure to mention the person who is streaming!')
            return

        streamerRole = None
        for role in ctx.guild.roles:
            if role.name == 'Colby College Gaming Streamer':
                streamerRole = role
                break

        message = f'{streamer.mention} is now live on twitch. Come check them out here:\n'
        twitch = f'https://www.twitch.tv/{twitchname}'
        if streamerRole in ctx.author.roles:
            message = '@everyone ' + message
        await ctx.send(message+twitch)


def setup(client):
    client.add_cog(Twitch(client))