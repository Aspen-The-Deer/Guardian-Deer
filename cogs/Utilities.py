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
            title="P.A.R.R.O.T. V.1.1.08/20 (6x734)"
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="What's New?", value="Added: \nUtility and Help commands. \nImproved formatting for embedded command outputs. \nBetter error handling! \nA cool new PfP!", inline=False)
        embed.add_field(name="Changes:", value="Limited social interactions to one user at a time. \nMusic player limited to one guild at a time. \nImprovements to the overall embedding format to make outputs look more professional.", inline=False)
        embed.add_field(name="Removed:", value="Lack of feedback upon command faliure. \nRemoved Herobrine", inline=False)
        embed.add_field(name="What's Next?", value="Unban Commands. \nFurther options for playing audio in a VC. \nImages to compliment social commands. \nNew additions to social commands.", inline=False)
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
            embed2.add_field(name=">Kick", value="The Guardian will kick the specified user for a specified reason.\n Usage: >ban [User Mention] [Kick reason]", inline=False)
            embed2.add_field(name=">Unban", value="NULL.", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed2)
            return
        elif module == "Music" or module == "music":
            embed2= discord.Embed(
                colour=(0x629632),
                title="Music Commands:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name=">Join", value="Connects the bot to your voice channel.", inline=False)
            embed2.add_field(name=">Leave", value="Disconnects the bot from it's current voice channel.", inline=False)
            embed2.add_field(name=">Play", value="Plays the audio from any video on YouTube. (Must be a Valid URL)\n Usage: >play [Youtube URL]", inline=False)
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
            embed2.add_field(name=">Exit", value="Manually stops the bot's client without needing to do so in the terminal.", inline=False)
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
            embed.add_field(name=">Help Music", value="This command returns help info for the Guardian's Music commands.", inline=False)
            embed.add_field(name=">Help Social", value="This command returns help info for the Guardian's Social commands.", inline=False)
            embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Utilities(client))