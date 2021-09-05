'''
Temperature.py

A cog file to hold functions for the Temperature events of the Colby Gaming Server
'''
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("\t- Temperature have loaded")

    @commands.command()
    async def ftoc(self, ctx, temp):
        try:
            temperature = (5 / 9) * (int(temp) - 32)
            string = "The temperature {}° Fahrenheit is {:.0f}° in Celsius".format(temp, temperature)
            await ctx.send(string)
        except Exception:
            await ctx.send(
                f"@{ctx.message.author}, a problem has been encountered with the input {ctx}\nPlease try again")

    @commands.command()
    async def ctof(self, ctx, temp):
        try:
            temperature = (int(temp) * (9 / 5)) + 32
            string = "The temperature {}° Celsius is {:.0f}° in Fahrenheit".format(temp, temperature)
            await ctx.send(string)
        except Exception:
            await ctx.send(
                f"@{ctx.message.author}, a problem has been encountered with the input {temp}\nPlease try again")


def setup(client):
    client.add_cog(Events(client))