import discord
import sys
import time
import random
import os
import github
import requests
import base64
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
    @commands.has_permissions(manage_messages=True)
    async def ban (self, ctx, member:discord.User=None, *, reason: str):
        server = ctx.guild.name
        mod = ctx.message.author.mention
        if member == None or member == ctx.message.author:
            embed = discord.Embed(title="The Ban Hammer", description=("You use the ban hammer, but it has no effect!"), color=(0x629632))
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
            embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.channel.send(embed=embed)
            embed2= discord.Embed(
                colour=(0x629632),
                title="You have been Banned:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name="You have been banned from:", value=str(server), inline=False)
            embed2.add_field(name="For the Reason:", value=str(reason), inline=False)
            embed2.add_field(name="You were Banned By:", value=str(mod), inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")
            await member.send(embed=embed2)


    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed4= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed4.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed4.add_field(name="Please enter a reason for the punishment.", value="Error: #002", inline=False)
            embed4.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed4)   
            return
        elif isinstance(error, commands.MissingPermissions):
            embed3= discord.Embed(
                colour=(0x629632),
                title="Insufficient Permissions..."
            )

            embed3.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed3.add_field(name="You are missing the permissions required to use this command.", value="Error: #001", inline=False)
            embed3.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed3)   
            return
        else:
            print(error)

    @commands.command(aliases =["Kick", "k", "K"])
    @commands.has_permissions(manage_messages=True)
    async def kick (self, ctx, member:discord.User=None, *, reason: str):
        server = ctx.guild.name
        mod = ctx.message.author.mention
        if member == None or member == ctx.message.author:
            embed3 = discord.Embed(title="The Cold Boot", description=("You try to kick yourself! And... Ouch... That looked like it hurt..."), color=(0x629632))
            await ctx.channel.send(embed=embed3)
            return
        elif reason != None:
            await ctx.guild.ban(member, reason=reason)
            embed= discord.Embed(
                colour=(0x629632),
                title="User Kicked:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="User:", value=str(member), inline=False)
            embed.add_field(name="Reason:", value=str(reason), inline=False)
            embed.add_field(name="Kicked By:", value=str(mod), inline=False)
            embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.channel.send(embed=embed)
            embed2= discord.Embed(
                colour=(0x629632),
                title="You have been Kicked:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name="You have been Kicked from:", value=str(server), inline=False)
            embed2.add_field(name="For the Reason:", value=str(reason), inline=False)
            embed2.add_field(name="You were kicked By:", value=str(mod), inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")
            await member.send(embed=embed2)


    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed4= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed4.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed4.add_field(name="Please enter a reason for the punishment.", value="Error: #002", inline=False)
            embed4.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed4)   
        elif isinstance(error, commands.MissingPermissions):
            embed3= discord.Embed(
                colour=(0x629632),
                title="Insufficient Permissions..."
            )

            embed3.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed3.add_field(name="You are missing the permissions required to use this command.", value="Error: #001", inline=False)
            embed3.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed3)   
            return
        else:
            print(error)

    @commands.command(aliases =["Unban", "u", "U"])
    @commands.guild_only()
    async def unban(self, ctx, *, userId):
        mod = ctx.message.author.mention
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
        embed= discord.Embed(
            colour=(0x629632)
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="User Pardoned by:", value=str(mod), inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

        await ctx.channel.send(embed=embed)
        return


    user_id = None
    guild_id = None
    reasons = None

    @commands.command(aliases = ['Warn', 'Strike', 'strike'])
    async def warn(self, ctx, userId, *, reason: str):
        global user_id, reasons, guild_id
        guild_id = ctx.message.guild.id
        user_id = userId
        reasons = reason
        direct = os.getcwd()
        os.chdir(direct)
        try:
            f = open("warns.txt", "a")
        except PermissionError:
            return "Invalid Permissions"
        else:
            with f:
                f.write(f"User: {user_id}, Warn Location: {guild_id}, Reason: {reasons}")
                print(str(user_id)+' In ' +str(guild_id)+ ' Has been Warned For: ' +str(reasons))
                gitHubFileName = ('warns.txt')
                fileName = ('warns.txt')
                repo_slug = ('Aspen-The-Deer/Guardian-Deer')
                branch = ('master')
                user = ('Aspen-The-Deer')
                token = (os.environ['GIT_TOKEN'])
                message = "Automated update " + str(datetime.datetime.now())
                path = "https://api.github.com/repos/%s/branches/%s" % (repo_slug, branch)

                r = requests.get(path, auth=(user,token))
                if not r.ok:
                    print("Error when retrieving branch info from %s" % path)
                    print("Reason: %s [%d]" % (r.text, r.status_code))
                rjson = r.json()
                treeurl = rjson['commit']['commit']['tree']['url']
                r2 = requests.get(treeurl, auth=(user,token))
                if not r2.ok:
                    print("Error when retrieving commit tree from %s" % treeurl)
                    print("Reason: %s [%d]" % (r2.text, r2.status_code))
                r2json = r2.json()
                sha = None

                for file in r2json['tree']:
                    # Found file, get the sha code
                    if file['path'] == gitHubFileName:
                        sha = file['sha']

                # if sha is None after the for loop, we did not find the file name!
                if sha is None:
                    print ("Could not find " + gitHubFileName + " in repos 'tree' ")
                    raise Exception

                with open(fileName, 'rb') as data:
                    content = base64.b64encode(data.read())

                # gathered all the data, now let's push
                inputdata = {}
                inputdata["path"] = str(gitHubFileName)
                inputdata["branch"] = str(branch)
                inputdata["message"] = str(message)
                inputdata["content"] = str(content)
                if sha:
                    inputdata["sha"] = str(sha)
                updateURL = "https://github.com/Aspen-The-Deer/Guardian-Deer" + gitHubFileName
                try:
                    rPut = requests.put(updateURL, auth=(user,token), data = json.dumps(inputdata))
                    if not rPut.ok:
                        print("Error when pushing to %s" % updateURL)
                        print("Reason: %s [%d]" % (rPut.text, rPut.status_code))
                        raise Exception
                except requests.exceptions.RequestException as e:
                    print ('Something went wrong! I will print all the information that is available so you can figure out what happend!')
                    print (rPut)
                    print (rPut.headers)
                    print (rPut.text)
                    print (e)

def setup(client):
    client.add_cog(Punishments(client))