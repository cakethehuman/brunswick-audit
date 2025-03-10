import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("dc bot/token.env")

        
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.command(name = "test")
async def test(ctx, arg):
    await ctx.send(arg)
    
@bot.command(name= "result")
async def result(ctx):
    await ctx.send("wait")
    
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

bot.run(os.getenv("TOKEN"))