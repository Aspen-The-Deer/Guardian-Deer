import discord
import sys
import random
import time
import datetime
from discord.ext import commands

class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Utilities.py')
        time.sleep(0.2)
        print(20 * '~')

    @commands.command(aliases=["Changelog", "log", "Log", "release", "Release", "Version", "version"])
    async def changelog(self, ctx):
        embed= discord.Embed(
            colour=(0x629632),
            title="P.A.R.R.O.T. V.1.2.1.20/20 (8c74832)"
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="What's New?", value="Added: Online hosting to allow the bot to run 24/7", inline=False)
        embed.add_field(name="Changes:", value="Social Command Interactions will be Permanantly limited to One.", inline=False)
        embed.add_field(name="Removed:", value=">play\n>join\n>leave", inline=False)
        embed.add_field(name="What's Next?", value="More Social Commands.\nLevelling System.\nWarning / Strike system", inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

        await ctx.send(embed=embed)

    @commands.command(aliases=["credits", "Cred", "cred"])
    async def Credits(self, ctx):
        embed= discord.Embed(
            colour=(0x629632),
            title="Credits!"
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="Description:", value="These are the primary contributors to the Guardian Bot who are credited below.", inline=False)
        embed.add_field(name="Beowulf#1863", value="Role: Owner\n Wrote the majority of code that allows the bot to function, as well as managing it's online hosting.", inline=False)
        embed.add_field(name="Mathew!#1404", value="Role: Code / Debug Manager\n Helped massively with polishing off and improving features as well as debugging broken code.", inline=False)
        embed.add_field(name="Aurora#0063", value="Role: Inspiration and Help with Initial Code.\n Inspired me to make this bot in the first place as well as teaching me the ropes with Discord bot creation in the first place.", inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

        await ctx.send(embed=embed)  

    @commands.command(aliases=["listerr", "Errors", "errors", "Error"])
    async def error(self, ctx):
        embed= discord.Embed(
            colour=(0x629632),
            title="Known Errors:"
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="#000", value="Unknown Errors.", inline=False)
        embed.add_field(name="#001", value="Missing Permissions.", inline=False)
        embed.add_field(name="#002", value="Missing Required Arguments.", inline=False)
        embed.add_field(name="#003", value="Coding Limitations.", inline=False)
        embed.add_field(name="#004", value="Precautionary Limitations.", inline=False)
        embed.add_field(name="#005", value="Command Does Not Exist.", inline=False)
        embed.add_field(name="#006", value="Unable To Complete Request.", inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

        await ctx.send(embed=embed)


    @commands.command(aliases=['help'])
    async def Help(self, ctx, *, module:str):
        if module == "Utilities" or module == "utilities":
            embed= discord.Embed(
                colour=(0x629632),
                title="Utility Commands:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name=">Ping", value="This command returns the current ping of the bot in milliseconds.", inline=False)
            embed.add_field(name=">Purge", value="Deletes a specified number of previous messages. \n Useage: >purge [# of Messages]", inline=False)
            embed.add_field(name=">Uptime", value="NULL.", inline=False)
            embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed)
            return
        elif module == "Moderation" or module == "moderation":
            embed2= discord.Embed(
                colour=(0x629632),
                title="Moderation Commands:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name=">Ban", value="The Guardian will ban the specified user for a specified reason.\n Usage: >ban [User Mention] [Ban reason]", inline=False)
            embed2.add_field(name=">Kick", value="The Guardian will kick the specified user for a specified reason.\n Usage: >kick [User Mention] [Kick reason]", inline=False)
            embed2.add_field(name=">Unban", value="The Guardian will unban the desired user.\n Useage: >unban [User ID]", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed2)
            return
        elif module == "Social" or module == "social":
            embed2= discord.Embed(
                colour=(0x629632),
                title="Social Commands:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name=">Hug", value="Allows you to hug another user.\n Usage: >hug [User Mention]", inline=False)
            embed2.add_field(name=">Cuddle", value="Allows you to cuddle another user.\n Usage: >cuddle [User Mention]", inline=False)
            embed2.add_field(name=">Boop", value="Allows you to boop another user.\n Usage: >boop [User Mention]", inline=False)
            embed2.add_field(name=">Flop", value="Allows you to flop on another user.\n Usage: >flop [User Mention]", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed2)
            return
        elif module == "dev" or module == "debug":
            embed2= discord.Embed(
                colour=(0x629632),
                title="Developer Commands:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name=">Error", value="Lists the meanings of all known error codes.", inline=False)
            embed2.add_field(name=">Changelog", value="Opens the latest change log.", inline=False)
            embed2.add_field(name=">Credits", value="Opens the credits page.", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed2)
            return

        else:
            embed2= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name="That Command Does Not Exist...", value="Error: #005", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed2)   

    @Help.error
    async def help_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed= discord.Embed(
                colour=(0x629632),
                title="Help Commands:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name=">Help", value="This command returns this embed.", inline=False)
            embed.add_field(name=">Help Utilities", value="This command returns help info for the Guardian's Utility commands.", inline=False)
            embed.add_field(name=">Help Moderation", value="This command returns help info for the Guardian's Moderation commands.", inline=False)
            embed.add_field(name=">Help Social", value="This command returns help info for the Guardian's Social commands.", inline=False)
            embed.add_field(name=">Help Social", value="This command returns help info for the Guardian's Developer commands.\nNote: These commands are simply related to information about the Development process of Guardian Deer.", inline=False)
            embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Utilities(client))