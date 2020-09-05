import discord
import datetime
import time
from discord.ext import commands

start_time = time.time()


class Timer(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Uptime.py')

    @commands.command(pass_context=True)
    @commands.cooldown(5, 3600, commands.BucketType.user)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed= discord.Embed(
            colour=(0x629632)
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name = ('Uptime'), value = (text))
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")
        try:
            await ctx.channel.send(embed=embed)
        except discord.HTTPException:
            await ctx.channel.send("Current uptime: " + text)


def setup(client):
    client.add_cog(Timer(client))