import discord
import sys
import time
from discord.ext import commands

class Shredder(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Shredder.py')


    @commands.command(aliases=['purge', 'Purge', 'Shred', 'clear', 'Clear'])
    @commands.has_permissions(manage_messages=True)
    async def shred(self, ctx, amount=5):
        if amount >= 101:
            embed= discord.Embed(
                colour=(0x629632)
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="An error has occurred...", value="You may only delete a maximum of 100 messages at a time!\n Error: #008", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=amount + 1)
            embed= discord.Embed(
                colour=(0x629632)
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="Shredder!", value="Shredded "+str(amount)+" messages!", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Shredder(client))