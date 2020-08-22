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


    async def update_data(self, users, user):
        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
            users[f'{user.id}']['experience'] = 0
            users[f'{user.id}']['level'] = 1


    async def add_experience(self, users, user, exp):
        users[f'{user.id}']['experience'] += exp


    async def level_up(self, users, user, message):
        with open('levels.json', 'r') as g:
            levels = json.load(g)
        experience = users[f'{user.id}']['experience']
        lvl_start = users[f'{user.id}']['level']
        lvl_end = int(experience ** (1 / 4))
        if lvl_start < lvl_end:
            await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
            users[f'{user.id}']['level'] = lvl_end

    @commands.Cog.listener()
    async def level(self, ctx, member: discord.Member = None):
        if not member:
            id = ctx.message.author.id
            with open('users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'You are at level {lvl}!')
        else:
            id = member.id
            with open('users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'{member} is at level {lvl}!')


def setup(client):
    client.add_cog(Levelling(client))