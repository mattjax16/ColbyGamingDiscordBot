'''
Events.py

A cog file to hold functions for the main events of the Colby Gaming Server
'''
import json
import os
import discord
import math
from discord import member, client
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("\t- Events have loaded")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('files/users.json', 'r') as f:
            users = json.load(f)

        channel = self.client.get_channel(777661356836782091)
        message = f':grin:  Welcome {str(member)[:-5]} to the Colby College Gaming Server  :grin:  '
        await channel.send(message)

        await update_data(users, member)

        with open('files/users.json', 'w') as f:
            json.dump(users, f)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(777661356836782091)
        message = f':sob: {str(member)[:-5]} has left the server :sob:'
        await channel.send(message)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return

        with open('files/users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)

        # TODO:
        # consider adding experience based on level
        # more research is required for this
        await add_experience(users, message.author, 3)
        await level_up(users, message.author, message.channel)

        with open('files/users.json', 'w') as f:
            json.dump(users, f)


async def update_data(users, user):
    userid = str(user.id)
    if userid not in users:
        users[userid] = {}
        users[userid]['experience'] = 0
        users[userid]['level'] = 0


async def add_experience(users, user, exp):
    userid = str(user.id)
    users[userid]['experience'] += exp


async def level_up(users, user, channel):
    userid = str(user.id)
    experience = users[userid]['experience']
    lvl_start = users[userid]['level']
    lvl_end = int(math.floor(0.25 * math.sqrt(experience)))

    if lvl_start < lvl_end:
        await channel.send('{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[userid]['level'] = lvl_end


def setup(client):
    client.add_cog(Events(client))
