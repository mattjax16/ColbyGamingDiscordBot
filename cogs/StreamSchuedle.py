'''
StreamSchuedle.py

A cog file to hold functions for the Twitch stream schuedles of the Colby Gaming Server
'''
from discord.ext import commands


class StreamSchuedle(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.list_scheduled = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('\t- Stream has loaded')

    @commands.command()
    async def tschedule(self, ctx, time, timezone, day):
        self.list_scheduled.append((time, timezone, day, str(ctx.message.author)[:-5]))
        await ctx.send(f"{str(ctx.message.author)[:-5]}, Stream has been Scheduled")

    @commands.command()
    async def scheduled(self, ctx):
        for i in range(len(self.list_scheduled)):
            await ctx.send(self.list_scheduled[i])

    @commands.command()
    async def removeSchedule(self, ctx, time, timezone, day, username):
        checking = [(ctx, time, timezone, day, username)]
        valid = False
        index = 0

        for i in range(0, len(self.list_scheduled)):
            for j in range(0, len(self.list_scheduled)):
                if checking[i][j] == self.list_scheduled[i][j]:
                    valid = True
                    index = i
                    break
        if valid:
            self.list_scheduled.pop(index)

        await ctx.send(f'str({ctx.message.author})[:-5] the scheduled stream has been removed')


def setup(client):
    client.add_cog(StreamSchuedle(client))