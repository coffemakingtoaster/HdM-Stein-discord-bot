import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json 

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="addevent",help="Use this to create events!")
@commands.has_role("bot dev")
async def on_message(ctx):
    
    


@bot.command(name="test",help="This is a test!")
@commands.has_role("bot dev")
async def on_message(ctx):
    await ctx.send("success")
    
bot.run(TOKEN)