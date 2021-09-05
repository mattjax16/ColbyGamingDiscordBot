'''
Updates.py

A cog file to hold functions for the Time events of the Colby Gaming Server
'''
import discord
from discord.ext import commands


class Update(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('\t- Update has loaded')

    @commands.command(name="ver")
    async def ver(self, ctx):
        await ctx.send("ColbyCollegeGamingDiscordBot VERSION: 1.01")

    @commands.command(name="patch")
    async def patch(self, ctx):
        await ctx.send("ColbyCollegeGamingDiscordBot VERSION: 1.01\n\n"
                       "COMMANDS:\n"
                       "1. Changed command \"hello\"\n\t\t"
                       "- prints the users name after\n"
                       "2. Changed Error message of command \"tconvert\"\n"
                       "\t\t- Added users name in the message\n"
                       "3. Added a welcome user event\n"
                       "4. Added a user leaving/kicked/removed event\n"
                       "5. Added a command \"tlive\"\n\t\t"
                       "- mentions everyone that you are live on twitch and links it\n\n"
                       "MISC:\n"
                       "1. Added categories in command \"help\"\n"
                       "2. Removed non commands in the help command")


def setup(client):
    client.add_cog(Update(client))