import discord
import datetime
import time
from discord.ext import commands

class Logging(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Logging.py')

    @commands.Cog.listener()
    async def on_message_edit(self, ctx, before, after, channel: discord.channel=None):
        member = ctx.message.author
        channel = channel
        logger = discord.utils.get(discord.guild.TextChannel, name="logs")
        if not after.author.bot:
            if before.content != after.content:
                embed= discord.Embed(
                    colour=(0x629632)
                )

                embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
                embed.add_field(name = ('Message Edited in:'), value = (channel))
                embed.add_field(name = ('Author:'), value = (member))
                embed.add_field(name = ('Before:'), value = (before))
                embed.add_field(name = ('After:'), value = (after))
                embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")
                await logger.send(embed=embed)


def setup(client):
    client.add_cog(Logging(client))