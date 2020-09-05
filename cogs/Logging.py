import discord
import datetime
from datetime import datetime
import time
from discord.ext import commands

guild = 0

class Logging(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Logging.py')

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        member = after.author.mention
        logger = discord.utils.get(after.guild.channels, name='logs')
        location = after.channel.mention
        if not after.author.bot:
            if before.content != after.content:
                embed= discord.Embed(
                    colour=(0x629632),
                    title = "Message Edited:"
                )

                embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
                embed.add_field(name = ('Author:'), value = (member), inline=False)
                embed.add_field(name = ('Before:'), value = ('"')+(before.content)+('"'), inline=False)
                embed.add_field(name = ('After:'), value = ('"')+(after.content)+('"'), inline=False)
                embed.add_field(name = ('In:'), value = (location), inline=False)
                embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")
                await logger.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        member = message.author.mention
        logger = discord.utils.get(message.guild.channels, name='logs')
        location = message.channel.mention
        if not message.author.bot:
            embed= discord.Embed(
                colour=(0x629632),
                title = "Message Deleted:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name = ('Author:'), value = (member), inline=False)
            embed.add_field(name = ('Message Content:'), value = ('"')+(message.content)+('"'), inline=False)
            embed.add_field(name = ('In:'), value = (location), inline=False)
            embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")
            await logger.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, ctx, member: discord.User=None):
        menti = member.mention
        logger = discord.utils.get(message.guild.channels, name='logs')
        server = ctx.guild.name
        embed= discord.Embed(
            colour=(0x629632),
            title = "Message Deleted:"
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name = ('User Joined:'), value = (menti)+(" has joined the server!"), inline=False)
        embed.add_field(name="Id:", value= member.id, inline=False)
        embed.add_field(name="Joined:", value= member.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Created:", value= member.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")
        await logger.send(embed=embed)


    @commands.command(aliases=["profile", "ui", "mi", "Profile"])
    async def user_info(self, ctx, target: discord.User=None):
        target = target or ctx.author
        menti = target.mention
        embed= discord.Embed(
            colour=(0x629632),
            title="User Profile:"
        )

        embed.set_thumbnail(url=target.avatar_url)
        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="Name:", value= menti, inline=False)
        embed.add_field(name="Id:", value= target.id, inline=False)
        embed.add_field(name="Highest Role:", value= target.top_role.mention, inline=False)
        embed.add_field(name="Status:", value= str(target.status).title(), inline=False)
        embed.add_field(name="Activity:", value= f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'Not doing anything right now.'} {target.activity.name if target.activity else ''}", inline=False)
        embed.add_field(name="Joined:", value= target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Created:", value= target.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Boosting Status:", value= bool(target.premium_since), inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")


        await ctx.send(embed=embed)

    @commands.command(aliases=["info", "si", "gi", "Info"])
    async def server_info(self, ctx):
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        embed= discord.Embed(
            colour=(0x629632),
            title="Guild Info:"
        )

        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="Name:", value= ctx.guild.name, inline=False)
        embed.add_field(name="Id:", value= ctx.guild.id, inline=False)
        embed.add_field(name="Region:", value= ctx.guild.region, inline=False)
        embed.add_field(name="Owner:", value= ctx.guild.owner.mention, inline=False)
        embed.add_field(name="Created:", value= ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Members:", value= len(ctx.guild.members), inline=False)
        embed.add_field(name="Humans:", value= len(list(filter(lambda m: not m.bot, ctx.guild.members))), inline=False)
        embed.add_field(name="Bots:", value= len(list(filter(lambda m: m.bot, ctx.guild.members))), inline=False)
        embed.add_field(name="Banned Users:", value= len(await ctx.guild.bans()), inline=False)
        embed.add_field(name="Statuses:", value= f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚫ {statuses[3]}", inline=False)
        embed.add_field(name="Text Channels:", value= len(ctx.guild.text_channels), inline=False)
        embed.add_field(name="Voice Channels:", value= len(ctx.guild.voice_channels), inline=False)
        embed.add_field(name="Categories:", value= len(ctx.guild.categories), inline=False)
        embed.add_field(name="Roles:", value= len(ctx.guild.roles), inline=False)
        embed.add_field(name="Invites:", value= len(await ctx.guild.invites()), inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Logging(client))