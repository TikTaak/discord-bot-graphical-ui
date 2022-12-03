from . import token

# discord liberary

import discord
from discord.ext import commands
from asyncio import *




class Config():
    prefix = "!"
    activity = "Hi Django"
    admin = ""

bot = commands.Bot(command_prefix='', intents=discord.Intents.all())

@bot.event
async def on_ready():
    # activeservers = client.guilds
    channel = bot.get_channel(963743048439832600)
    await channel.send("DOoooon!!!!")
    await bot.change_presence(activity=discord.Game(name=Config.activity))
    print("Bot ready")

@bot.command()
async def a(ctx):
    print("done")
    await ctx.send(" FVFVDFVDFV.")

bot.run(token.Token.TOKEN)
