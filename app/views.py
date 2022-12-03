from django.shortcuts import render
from django.http import HttpResponse
from . import token
# discord liberary
import discord
from discord.ext import commands
from asyncio import *

#######----------------------#######

def app(request):
    return render(request, 'index.html', {})

def send(request):
    print("Done !!!")
    return HttpResponse('Message sent successfully')

#######----------------------#######


class Config():
    prefix = "!"
    activity = "Hi Django"
    admin = ""

bot = commands.Bot(command_prefix='', intents=discord.Intents.all())

@bot.event
async def on_ready():
    # activeservers = client.guilds
    await bot.change_presence(activity=discord.Game(name=Config.activity))
    print("Bot ready")
    


@bot.command()
async def a(ctx):
    print("done")
    await ctx.send(" FVFVDFVDFV.")




bot.run(token.Token.TOKEN)
