import discord
import datetime
import time
from discord.ext import commands

start_time = time.time()


class Uptime(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Uptime.py')

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Sponsored by altcointrain.com - Choo!!! Choo!!!")
        try:
            await ctx.channel.send(embed=embed)
        except discord.HTTPException:
            await ctx.channel.send("Current uptime: " + text)


def setup(client):
    client.add_cog(Uptime(client))