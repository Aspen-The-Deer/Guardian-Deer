import discord
import sys
import random
import time
import json
import requests
from discord.ext import commands

class Hugs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Hugs.py')
    
    @commands.command(aliases=['Hug'])
    async def hug(self, ctx, check):
        user = ctx.message.mentions[0]
        if len(ctx.message.mentions) <= 1:
            responses = ["{} gives warm hugs to {}!", "{} notices {}'s lack of hugs, and hugs them!", "{} gives {} a big ol' hug!", "{} gives the best hugs, and they give them all to {}!", "{} shouts 'TACTICAL HUGS INCOMING!' as they hug tackle {}!", "{} sneakily hugs {}!", "{} asked for hugs from {} and got what they wanted!", "{} hug tackled {} unexpectedly!", "{} spotted {} and ran up to them for hugs!", "{} felt really lonely until {} hugged them from behind!"]
            choice = random.choice(responses)
            choice = choice.format(ctx.message.author.mention, user.mention)
            embed= discord.Embed(
                colour=(0x629632)
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            http_body = requests.get("https://api.furry.bot/v2/furry/hug")
            http_json = json.loads(http_body.content)
            json_images = http_json["images"]
            json_images_parse = json_images[0]
            embed.set_image(url=json_images_parse["shortURL"])
            embed.add_field(name="Hugs!", value=(choice), inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
        elif len(ctx.message.mentions) > 1:
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="You may only hug one person at a time!", value="Error: #003", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
            return
        

    @commands.command(aliases=['Cuddle'])
    async def cuddle(self, ctx, check):
        user = ctx.message.mentions[0]
        if len(ctx.message.mentions) <= 1:
            responses = ["{} cuddles {} warmly!", "{} cuddled with {} while watching a movie...", "{} spent all night cuddling {}!", "{} cuddled {} supportively!", "{} cuddled {} with all their love and might!", "{} noticed {} was lonely, and decided to give them amazing cuddles!", "{} purred softly as they gave loving cuddles to {}.", "{} dived on to {}! Cuddling them tight!", "{} pulled {} into their pillow fort for warm cuddles!", "{} marched up to {} demanding their daily cuddles, They soon got what they asked for!"]
            choice = random.choice(responses)
            choice = choice.format(ctx.message.author.mention, user.mention)
            embed= discord.Embed(
                colour=(0x629632)
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            http_body = requests.get("https://api.furry.bot/v2/furry/cuddle")
            http_json = json.loads(http_body.content)
            json_images = http_json["images"]
            json_images_parse = json_images[0]
            embed.set_image(url=json_images_parse["shortURL"])
            embed.add_field(name="Cuddles!", value=(choice), inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
        elif len(ctx.message.mentions) > 1:
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="You may only Cuddle one person at a time!", value="Error: #003", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
            return


    @commands.command(aliases=['Boop'])
    async def boop(self, ctx, check):
        user = ctx.message.mentions[0]
        if len(ctx.message.mentions) <= 1:
            responses = ["{} ran up to {}, booped them, and ran away!", "{} gave {} a quick snoot boop!", "{} would boop {} repeatedly!", "{} stealthily boops {} before disappearing into the night...", "{} gave {} some well deserved and loving boops!", "{} booped {} lovingly!", "{} excitedly booped {}!", "{} booped {}!"]
            choice = random.choice(responses)
            choice = choice.format(ctx.message.author.mention, user.mention)
            embed= discord.Embed(
                colour=(0x629632)
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            http_body = requests.get("https://api.furry.bot/v2/furry/boop")
            http_json = json.loads(http_body.content)
            json_images = http_json["images"]
            json_images_parse = json_images[0]
            embed.set_image(url=json_images_parse["shortURL"])
            embed.add_field(name="Boops!", value=(choice), inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
        elif len(ctx.message.mentions) > 1:
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="You may only boop one person at a time!", value="Error: #003", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
            return

    @commands.command(aliases=['Flop'])
    async def flop(self, ctx, check):
        user = ctx.message.mentions[0]
        if len(ctx.message.mentions) <= 1:
            responses = ["{} was searching for {} for ages, just so they could flop on them!\nHow cute!", "{} did a hecka big flop onto {}!", "{} flopped graciously on to {}!", "{} flopped happily infront of a surprised {}!", "Flopping was {}'s specialty, and they wanted to show off their skills to {}!", "{} happily flopped into {}'s arms!" ]
            choice = random.choice(responses)
            choice = choice.format(ctx.message.author.mention, user.mention)
            embed= discord.Embed(
                colour=(0x629632)
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            http_body = requests.get("https://api.furry.bot/v2/furry/flop")
            http_json = json.loads(http_body.content)
            json_images = http_json["images"]
            json_images_parse = json_images[0]
            embed.set_image(url=json_images_parse["shortURL"])
            embed.add_field(name="Flop!", value=(choice), inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
        elif len(ctx.message.mentions) > 1:
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="You may only flop on one person at a time!", value="Error: #003", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
            return

    @commands.command(aliases=['Kiss'])
    async def kiss(self, ctx, check):
        user = ctx.message.mentions[0]
        if len(ctx.message.mentions) <= 1:
            responses = ['{} smooches {} with love and passion']
            choice = random.choice(responses)
            choice = choice.format(ctx.message.author.mention, user.mention)
            embed= discord.Embed(
                colour=(0x629632)
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            http_body = requests.get("https://api.furry.bot/v2/furry/kiss")
            http_json = json.loads(http_body.content)
            json_images = http_json["images"]
            json_images_parse = json_images[0]
            embed.set_image(url=json_images_parse["shortURL"])
            embed.add_field(name="Kiss!", value=(choice), inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
        elif len(ctx.message.mentions) > 1:
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="You may only kiss one person at a time!", value="Error: #003", inline=False)
            embed.set_footer(text="Type '>help' for help options!") 
            await ctx.send(embed=embed)   
            return

        
    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.CheckAnyFailure):
            print("An unknown error occurred in Hugs.py")
        else:
            print(error)
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="This command requires you to mention another user!", value="Error: #002", inline=False)
            embed.set_footer(text="Type '>help' for help options!") 
            await ctx.send(embed=embed)   
            return

    @cuddle.error
    async def cuddle_error(self, ctx, error):
        if isinstance(error, commands.CheckAnyFailure):
            print("An unknown error occurred in Hugs.py")
        else:
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="This command requires you to mention another user!", value="Error: #002", inline=False)
            embed.set_footer(text="Type '>help' for help options!") 
            await ctx.send(embed=embed)   
            return

    @boop.error
    async def boop_error(self, ctx, error):
        if isinstance(error, commands.CheckAnyFailure):
            print("An unknown error occurred in Hugs.py")
        else:
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="This command requires you to mention another user!", value="Error: #002", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
            return

    @flop.error
    async def flop_error(self, ctx, error):
        if isinstance(error, commands.CheckAnyFailure):
            print("An unknown error occurred in Hugs.py")
        else:
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="This command requires you to mention another user!", value="Error: #002", inline=False)
            embed.set_footer(text="Type '>help' for help options!") 
            await ctx.send(embed=embed)   
            return

    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, commands.CheckAnyFailure):
            print("An unknown error occurred in Hugs.py")
        else:
            embed= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name="This command requires you to mention another user!", value="Error: #002", inline=False)
            embed.set_footer(text="Type '>help' for help options!")
            await ctx.send(embed=embed)   
            return

def setup(client):
    client.add_cog(Hugs(client))
