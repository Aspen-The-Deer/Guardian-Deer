import discord
import os
import sys
import time
from discord.ext import commands

client = commands.Bot(command_prefix = '>')
client.remove_command('help')


@client.command(aliases=['Exit'], pass_context = True)
async def exit(ctx):
    if str(ctx.message.author.id) == '606855758612660327':
        embed2= discord.Embed(
            colour=(0x629632),
            title="Shutting Down..."
        )

        embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed2.add_field(name="The bot has been manually stopped via Discord", value="Thank you for using me!", inline=False)
        embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
        await ctx.send(embed=embed2)   
        activity = discord.Game(name="with the off button...", type=2)
        await client.change_presence(status=discord.Status.online, activity=activity)
# Utilises the sys import to quickly shut off the bot using the discord client rather than the terminal
        sys.exit('The bot has been manually stopped via Discord')
    else:
            embed3= discord.Embed(
                colour=(0x629632),
                title="Insufficient Permissions..."
            )

            embed3.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed3.add_field(name="You are missing the permissions required to use this command.", value="Error: #001", inline=False)
            embed3.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed3)   

@client.command()
@commands.has_permissions(manage_messages=True)
async def load(ctx, ext):
    client.load_extension(f'cogs.{ext}')
    print('Extension Loaded')

@client.command()
@commands.has_permissions(manage_messages=True)
async def unload(ctx, ext):
    client.unload_extension(f'cogs.{ext}')
    print('Extension Un-Loaded')

# This is what looks for and opens all of the command modules (cogs)
for filename in os.listdir('C:/Users/jonah/Documents/Wulf Bot/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command(aliases=['Ping'])
async def ping(ctx):
# client.latency is given in seconds, hence it needs to be multiplied by 1000 to display in ms
    ping = round(client.latency * 1000)
    embed2= discord.Embed(
        colour=(0x629632)
    )

    embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
    embed2.add_field(name="Ping!", value=str(ping)+" ms", inline=False)
    embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
    await ctx.channel.send(embed=embed2)  

# Trigger for when the bot has launched, an indicator to tell me nothing has gone wrong
@client.event
async def on_ready():
# Sets the bot status
    activity = discord.Game(name="in the forest!", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(20 * '~')
    print('Logged in as:')
    print(client.user.name, '#6550')
    print(10 * '-')
    print('Command modules loaded:')



client.run(os.environ['DISCORD.TOKEN'])