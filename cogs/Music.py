import time
import discord
import youtube_dl
import os
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    players = {}

    @commands.Cog.listener()
    async def on_ready(self):
        scheck = os.path.isfile("audio.mp3")
        time.sleep(0.2)
        print('Music.py')
        try:
            if scheck:
                os.remove("audio.mp3")
                print ('Music.py: Removed Old Audio Files')
        except PermissionError:
            print('Music.py: File Cannot Be Deleted At This Time')
        except FileNotFoundError:
            print('Music.py: Specified File Does Not Exist')

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(pass_context = True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, *, url: str):
        scheck = os.path.isfile("audio.mp3")
        try:
            if scheck:
                os.remove("audio.mp3")
                print ('Removed old song file')
        except PermissionError:
            print ('Guild Play limit Reached. #004')
            embed4= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed4.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed4.add_field(name="Due to current limitations, I can only play music in one guild at a time. Sorry for the inconvenience.", value="Error: #003", inline=False)
            embed4.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed4)   
            return
        try:
            if scheck == False:
                await ctx.channel.purge(limit=1)
                embed3= discord.Embed(
                    colour=(0x629632)
                )

                embed3.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
                embed3.add_field(name="Just one moment!", value="Your song request has been recieved and will start playing shortly!", inline=False)
                embed3.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
                await ctx.send(embed=embed3)  


                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }

                with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
                    print("Downloading audio files...\n")
                    ydl.download([url])

                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        name = file
                        print(f"Renamed File: {file}\n")
                        os.rename(file, "audio.mp3")

                ctx.voice_client.play(discord.FFmpegPCMAudio("audio.mp3"), after=lambda e: print(f"{name} has finished playing"))
                ctx.voice_client.source = discord.PCMVolumeTransformer(ctx.voice_client.source)
                ctx.voice_client.source.volume = 0.1

                embed3= discord.Embed(
                    colour=(0x629632)
                )

                embed3.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
                embed3.add_field(name="Now Playing!", value="Your song has been processed and will start playing shortly!", inline=False)
                embed3.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
                await ctx.send(embed=embed3)  
                print("Now Playing\n")
                return
        except FileExistsError:
            print ('Guild Play limit Reached. #004')
            embed4= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed4.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed4.add_field(name="Due to current limitations, I can only play music in one guild at a time. Sorry for the inconvenience.", value="Error: #003", inline=False)
            embed4.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed4)   

    @play.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed4= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed4.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed4.add_field(name="Please enter a valid YouTube URL.", value="Error: #002", inline=False)
            embed4.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed4)   
            
    @join.error
    async def join_error(self, ctx, error):
        if isinstance(error, commands.CheckAnyFailure):
            print("An unknown error occurred in Music.py")
        else:
            embed4= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed4.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed4.add_field(name="The bot is alredy connected elsewhere in this server!", value="Error: #006", inline=False)
            embed4.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed4)   

    @leave.error
    async def leave_error(self, ctx, error):
        if isinstance(error, commands.CheckAnyFailure):
            print("An unknown error occurred in Music.py")
        else:
            embed4= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed4.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed4.add_field(name="The bot is not currently connected to any voice channel!", value="Error: #006", inline=False)
            embed4.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed4)  
            

def setup(client):
    client.add_cog(Music(client))