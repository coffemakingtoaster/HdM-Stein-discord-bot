import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json 
import discord_events

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PATH = os.getenv('FILE_PATH')
bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="listevent", help ="Use this to list all events!")
@commands.has_role("bot dev")
async def on_message(ctx):
    event_list = discord_events.events.list()
    message = ""
    for item in event_list:
        message+= item["event_name"]+"\t"+item["event_date"]+"\t"+str(len(item["event_participants"]))+"\n"
    await channel.send(message)
        

@bot.command(name="addevent",help="Use this to create events! This requires 2 parameters the Eventname (in quotation marks) and the event_date (DD/MM/YYYY:HH:MM). Use !addeventdesc")
@commands.has_role("bot dev")
async def on_message(ctx,event_name,event_date):
    if event_name and event_date:
        uID = discord_events.events.generate_event(event_name,event_date)
        await channel.send("Event was succcessfully generated and added to the db! Your EventID is ",uID)
        
    


@bot.command(name="test",help="This is a test!")
@commands.has_role("bot dev")
async def on_message(ctx):
    await ctx.send("success")
    
bot.run(TOKEN)