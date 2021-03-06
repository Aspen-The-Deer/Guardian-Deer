import discord
import sys
import time
import random
import os
import json
import datetime
from discord.ext import commands

class Punishments(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Punish.py')



    @commands.command(aliases =["Ban", "b", "B"])
    @commands.has_permissions(ban_members=True)
    async def ban (self, ctx, member:discord.User=None, reason:str=None):
        logger = discord.utils.get(ctx.guild.channels, name='logs')
        server = ctx.message.guild
        mod = ctx.message.author.mention
        embed2= discord.Embed(
            colour=(0x629632),
            title="You have been Banned:"
        )

        embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed2.add_field(name="You have been banned from:", value=str(server), inline=False)
        embed2.add_field(name="For the Reason:", value=str(reason), inline=False)
        embed2.add_field(name="You were Banned By:", value=str(mod), inline=False)
        embed2.set_footer(text="Type '>help' for help options!")
        if member == None or member == ctx.message.author:
            embed= discord.Embed(
                colour=(0x629632),
                title="User Cannot Banned:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="User:", value=str(member), inline=False)
            embed.add_field(name="This happened because:", value="You cannot ban yourself.\nNo user was specified to ban.", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.channel.send(embed=embed)
            return
        elif reason != None:
            await ctx.guild.ban(member, reason=reason)
            embed= discord.Embed(
                colour=(0x629632),
                title="User Banned:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="User:", value=str(member), inline=False)
            embed.add_field(name="Reason:", value=str(reason), inline=False)
            embed.add_field(name="Banned By:", value=str(mod), inline=False)
            embed.set_footer(text="Type '>help' for help options!")

            await ctx.channel.send(embed=embed)
        elif reason == None:
            reason = "No Reason Given"
            await ctx.guild.ban(member, reason=reason)
            embed= discord.Embed(
                colour=(0x629632),
                title="User Banned:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="User:", value=str(member), inline=False)
            embed.add_field(name="Reason:", value=str(reason), inline=False)
            embed.add_field(name="Banned By:", value=str(mod), inline=False)
            embed.set_footer(text="Type '>help' for help options!")

            await ctx.channel.send(embed=embed)
        try:
            await logger.send(embed=embed)
            await member.send(embed=embed2)
        except AttributeError:
            print("No logging channel found in "+server+", Ignoring Event.")
            await member.send(embed=embed2)



    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed3= discord.Embed(
                colour=(0x629632),
                title="Insufficient Permissions..."
            )

            embed3.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed3.add_field(name="You are missing the permissions required to use this command.", value="Error: #001", inline=False)
            embed3.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed3)   
            return
        else:
            print(error)

    @commands.command(aliases =["Kick", "k", "K"])
    @commands.has_permissions(kick_members=True)
    async def kick (self, ctx, member:discord.User=None,  reason:str=None):
        logger = discord.utils.get(ctx.guild.channels, name='logs')
        server = ctx.message.guild
        mod = ctx.message.author.mention
        embed2= discord.Embed(
            colour=(0x629632),
            title="You have been Kicked:"
        )

        embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed2.add_field(name="You have been Kicked from:", value=str(server), inline=False)
        embed2.add_field(name="For the Reason:", value=reason, inline=False)
        embed2.add_field(name="You were kicked By:", value=str(mod), inline=False)
        embed2.set_footer(text="Type '>help' for help options!")
        if member == None or member == ctx.message.author:
            embed= discord.Embed(
                colour=(0x629632),
                title="User Cannot Kicked:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="User:", value=str(member), inline=False)
            embed.add_field(name="This happened because:", value="You cannot kick yourself.\nNo user was specified to kick.", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.channel.send(embed=embed)
        elif reason != None:
            await ctx.guild.kick(member, reason=reason)
            embed= discord.Embed(
                colour=(0x629632),
                title="User Kicked:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="User:", value=str(member), inline=False)
            embed.add_field(name="Reason:", value=reason, inline=False)
            embed.add_field(name="Kicked By:", value=str(mod), inline=False)
            embed.set_footer(text="Type '>help' for help options!")

            await ctx.channel.send(embed=embed)
            embed2= discord.Embed(
                colour=(0x629632),
                title="You have been Kicked:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name="You have been Kicked from:", value=str(server), inline=False)
            embed2.add_field(name="For the Reason:", value=reason, inline=False)
            embed2.add_field(name="You were kicked By:", value=str(mod), inline=False)
            embed2.set_footer(text="Type '>help' for help options!")
            await member.send(embed=embed2)
        elif reason == None:
            reason = "No Reason Given"
            await ctx.guild.kick(member, reason=reason)
            embed= discord.Embed(
                colour=(0x629632),
                title="User Kicked:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="User:", value=str(member), inline=False)
            embed.add_field(name="Reason:", value=str(reason), inline=False)
            embed.add_field(name="Kicked By:", value=str(mod), inline=False)
            embed.set_footer(text="Type '>help' for help options!")

            await ctx.channel.send(embed=embed)
        try:
            await logger.send(embed=embed)
            await member.send(embed=embed2)
        except AttributeError:
            print("No logging channel found in "+server+", Ignoring Event.")
            await member.send(embed=embed2)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed3= discord.Embed(
                colour=(0x629632),
                title="Insufficient Permissions..."
            )

            embed3.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed3.add_field(name="You are missing the permissions required to use this command.", value="Error: #001", inline=False)
            embed3.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed3)   
            return
        else:
            print(error)

    @commands.command(aliases =["Unban", "u", "U"])
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def unban(self, ctx, *, userId):
        logger = discord.utils.get(ctx.guild.channels, name='logs')
        mod = ctx.message.author.mention
        server = ctx.message.guild
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
        embed= discord.Embed(
            colour=(0x629632)
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="User Pardoned by:", value=str(mod), inline=False)
        embed.set_footer(text="Type '>help' for help options!")

        await ctx.channel.send(embed=embed)
        try:
            await logger.send(embed=embed)
        except AttributeError:
            print("No logging channel found in "+server+", Ignoring Event.")
        return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed3= discord.Embed(
                colour=(0x629632),
                title="Insufficient Permissions..."
            )

            embed3.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed3.add_field(name="You are missing the permissions required to use this command.", value="Error: #001", inline=False)
            embed3.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed3)   
            return
        else:
            print(error)

def setup(client):
    client.add_cog(Punishments(client))