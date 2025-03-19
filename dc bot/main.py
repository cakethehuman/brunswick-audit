import discord
from discord.ext import commands

import os
import random
from dotenv import load_dotenv

from objects import footer_text,Format,bot


load_dotenv("dc bot/token.env")
        
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    
    
#Fun commands
@bot.command(name='hello')
async def hello(ctx):
    embed = Format("Hello","Hello there").command_maker()
    embed.set_footer(text=random.choice(footer_text))
    await ctx.send(embed=embed)
    
# Audit commands
@bot.command(name= "result")
async def result(ctx):
    embed = Format("Result","Result for the week").command_maker()
    file=discord.File("special spikey/avg2.csv")
    embed.set_footer(text=random.choice(footer_text))
    await ctx.send(embed=embed,file=file)
 
@bot.command(name='attendance')
async def attendance(ctx):
    embed = Format("Attendance","Attendance for the week").command_maker()
    file = discord.File("special spikey/attadance_by_name.png", filename="attadance_by_name.png")
    embed.set_image(url="attachment://attadance_by_name.png")
    await ctx.send(embed=embed,file=file)

#help/fuctional commands
    
@bot.command(name="cmd")
async def cmd(ctx):
    embed = Format("Commands","Commands for the bot").command_maker()
    embed.add_field(name="$hello", value="Greets the user", inline=False)
    embed.add_field(name="$attendance", value="Shows the attendance for the week", inline=False)
    embed.add_field(name="$result", value="Shows the result of the week", inline=False)
    embed.add_field(name="$update", value="Shows the update of the week", inline=False)
    embed.add_field(name="$kda", value="Shows the kda of the week", inline=False)
   
    await ctx.send(embed=embed)
    
    
@bot.command(name="update")
async def update(ctx):
    embed = Format("Update","Update the bot data but no done still beta").command_maker()
    await ctx.send(embed=embed)
    
@bot.command(name="kda")
async def kda(ctx):
    embed = Format("KDA","KDA of the week").command_maker()
    file = discord.File("special spikey\kda_info.csv", filename="kda_info.csv")
    await ctx.send(embed=embed,file=file)

bot.run(os.getenv("TOKEN"))