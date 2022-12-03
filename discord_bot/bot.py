from . import token
import time
# discord liberary

import discord
from discord.ext import commands
from asyncio import *




class Config():
    prefix = "!"
    activity = "Hi Django"
    admin = ""

bot = commands.Bot(command_prefix='', intents=discord.Intents.all())

# def send_message_channel(message, id):
def send_message_channel():
    print("send_message_channel")
    # channel = bot.get_channel(963743048439832600)
    # channel.send("DOoooon!!!!")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=Config.activity))
    print("Bot ready")

@bot.command()
async def a(ctx):
    channel = bot.get_channel(963743048439832600)
    await channel.send("DOoooon!!!!")
    print("done")
    await ctx.send(" FVFVDFVDFV.")

# time.sleep(10)
def run_bot():
    bot.run(token.Token.TOKEN)
  

