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
    await ctx.send(file=discord.File("special spikey/avg.csv"))
 
    
@bot.command(name='hello')
async def hello(ctx):
    embed = discord.Embed(title="Hello", 
                          description=f"Hello, {ctx.author.name}!", 
                          color= 10070709
                          )
    embed.set_footer(text="this is kinda cool")
    embed.set_author(name="Cake`s audit bot")

    await ctx.send(embed=embed)

@bot.command(name='attendance')
async def attendance(ctx):
    embed = discord.Embed(
        title="Attendance",
        description="Attendance for the week",
        color=6179726
    )
    embed.set_footer(text="Cool looking graph?")
    embed.set_author(name="Cake`s audit bot")
    file = discord.File("special spikey/attadance_by_name.png", filename="attadance_by_name.png")
    #embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/898978013013573376/898978040013383424/attendance.png")
    embed.set_image(url="attachment://attadance_by_name.png")
    await ctx.send(embed=embed,file=file)

bot.run(os.getenv("TOKEN"))