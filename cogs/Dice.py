import discord
import random
import time
from discord.ext import commands

class Dice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Dice.py')

    @commands.command(aliases = ['Roll'])
    async def roll(self, ctx, *, message:str):
        dice_num = message[:1]
        dice_type = message[2:]
        roll_num = 0
        total = 0
        print(dice_type)
        print(dice_num)
        while roll_num < int(dice_num):
            roll = random.randint(1,int(dice_type))
            total = total + roll
            roll_num += 1
            if roll_num == int(dice_num):
                break
        print(total)
        if int(dice_num) == 1:
            dice = ('Rolling '+str(dice_num)+' d'+str(dice_type))
        else:
            dice = ('Rolling '+str(dice_num)+' d'+str(dice_type)+"'s")
        responses = ('{} rolled a {}!')
        responses = responses.format(ctx.message.author.mention, total)
        embed= discord.Embed(
        colour=(0x744d3b)
        )

        embed.set_author(name="DnD Deer", icon_url="https://media.discordapp.net/attachments/745442555189133335/748694161187930223/aspenimg.png")
        embed.add_field(name = (dice), value = (responses))
        embed.set_footer(text="Type 'dnd help' for a list of commands!") 
        await ctx.channel.send(embed=embed)
        

def setup(client):
    client.add_cog(Dice(client))