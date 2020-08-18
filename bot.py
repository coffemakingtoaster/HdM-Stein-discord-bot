import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands,tasks
import json 
import discord_events
from aiofiles.os import remove

load_dotenv()


TOKEN = os.getenv('DISCORD_TOKEN')
PATH = os.getenv('FILE_PATH')
bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    bot.loop.create_task(cleanup())

@bot.command(name="listevent", help ="Use this to list all events!")
@commands.has_role("bot dev")
async def on_message(ctx):
    event_list = discord_events.events.list(os.getcwd())
    message = ""
    for i in event_list:
        item = event_list[i]
        print(item)
        message+= item["event_name"]+"\t"+item["event_date"]+"\t"+str(len(item["event_participants"]))+"\n"
    await ctx.send(message)
        

@bot.command(name="addevent",help="Use this to create events! This requires 2 parameters the Eventname (in quotation marks) and the event_date (DD/MM/YYYY:HH:MM). Use !addeventdesc")
@commands.has_role("bot dev")
async def on_message(ctx,event_name,event_date):
    if event_name and event_date:
        uID = discord_events.events.generate_event(os.getcwd(),event_name,event_date)
        await ctx.send("Event was succcessfully generated and added to the db! Your EventID is "+str(uID))
        
    

@bot.command(name="test",help="This is a test!")
@commands.has_role("bot dev")
async def on_message(ctx):
    await ctx.send("success")


async def cleanup():
    print("scanning for past events!")
    garbage = discord_events.events.garbage_collect(os.getcwd()) 
    for i in garbage:
        await remove(os.path.join(os.getcwd(),i))
    print("removed "+str(len(garbage))+" items!")
    await asyncio.sleep(30)


    
bot.run(TOKEN)