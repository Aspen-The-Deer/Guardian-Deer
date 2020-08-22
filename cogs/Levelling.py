import discord
import json
import os
import time
from discord.ext import commands

class Levelling(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Levelling.py')
        die = os.getcwd()
        os.chdir(die)

    @commands.Cog.listener()
    async def on_member_join(self, discord_member):
        with open('xp.json', 'r') as f:
            xp = json.load(f)

        await update_data(xp, member)

        with open('xp.json', 'w') as f:
            json.dump(xp, f)

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('xp.json', 'r') as f:
            xp = json.load(f)

        await update_data(xp, message.author)
        await add_xp(xp, message.author, 5)
        await level_up(xp, message.author)

        with open('xp.json', 'w') as f:
            json.dump(xp, f)


    async def update_data(self, xp, user):
        if not user.id in xp:
            xp[user.id] = {}
            xp[user.id]['experience'] = 0
            xp[user.id]['level'] = 0

    async def add_xp(self, xp, user, exp):
        xp[user.id]['experience'] += exp

    async def level_up(self, xp, user, channel):
        experience = xp[user.id]['experience']
        lvl_start = xp[user.id]['level']
        lvl_end = int(experience ** (1/4)) 

        if lvl_start < lvl_end:
            print('Level Up!')
            xp[user.id]['level'] = lvl_end


def setup(client):
    client.add_cog(Levelling(client))