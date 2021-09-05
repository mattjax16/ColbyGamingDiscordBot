'''
Times.py

A cog file to hold functions for the Time events of the Colby Gaming Server
'''
from discord.ext import commands

from datetime import datetime
import pytz


class Times(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('\t- Time is loaded')

    @commands.command(name="tconvert")
    async def tconvert(self, ctx, current_timezone, converted_timezone):
        try:
            user = ctx.message.author

            current = str(format(datetime.now(pytz.timezone(current_timezone.upper())), "%I:%M %p"))
            converted = str(format(datetime.now(pytz.timezone(converted_timezone.upper())), "%I:%M %p"))
            result = current + " " + current_timezone.upper() + " is " + converted + " " + converted_timezone.upper()
            await ctx.send(result)

        except pytz.exceptions.UnknownTimeZoneError as err:
            await ctx.send(
                f"Error: @{user} timezone {err} not found, please visit this site for valid timezones: \nhttps://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568\n")
        except:
            await ctx.send("Error: Please contact LaMoldy on discord")


def setup(client):
    client.add_cog(Times(client))