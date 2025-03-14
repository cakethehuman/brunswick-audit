import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("dc bot/token.env")

        
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

footer_text = ["Dawn is small","Seabiper","Polko is a guy or girl?","Spikey forgort to give me audit","diddydowa","Kazuyuki leading?","james what?"]

color_codes = [
    16777215,  # White (#FFFFFF)
    10070709,  # Greyple (#99AAb5)
    2303786,   # Black (#23272A)
    2895667,   # DarkButNotBlack (#2C2F33)
    2303786,   # NotQuiteBlack (#23272A)
    5793266,   # Blurple (#5865F2)
    5763719,   # Green (#57F287)
    16705372,  # Yellow (#FEE75C)
    15418782,  # Fuchsia (#EB459E)
    15548997,  # Red
]

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    
    
#Fun commands
@bot.command(name='hello')
async def hello(ctx):
    embed = discord.Embed(title="Hello", 
                          description=f"Hello, {ctx.author.name}!", 
                          color= random.choice(color_codes)
                          )
    embed.set_footer(text=random.choice(footer_text))
    embed.set_author(name="Cake`s audit bot")

    await ctx.send(embed=embed)
    
# Audit commands
@bot.command(name= "result")
async def result(ctx):
    embed = discord.Embed(
        title="Result",
        description="Result for the week",
        color= random.choice(color_codes)
    )
    file=discord.File("special spikey/avg2.csv")
    embed.set_footer(text=random.choice(footer_text))
    await ctx.send(embed=embed,file=file)
 
@bot.command(name='attendance')
async def attendance(ctx):
    embed = discord.Embed(
        title="Attendance",
        description="Attendance for the week",
        color= random.choice(color_codes)
    )
    embed.set_footer(text=random.choice(footer_text))
    embed.set_author(name="Cake`s audit bot")
    file = discord.File("special spikey/attadance_by_name.png", filename="attadance_by_name.png")

    embed.set_image(url="attachment://attadance_by_name.png")
    await ctx.send(embed=embed,file=file)

#help/fuctional commands
    
@bot.command(name="cmd")
async def cmd(ctx):
    embed = discord.Embed(
        title="Help",
        description="List of commands",
        color= random.choice(color_codes)
    )
    embed.add_field(name="$hello", value="Greets the user", inline=False)
    embed.add_field(name="$attendance", value="Shows the attendance for the week", inline=False)
    embed.add_field(name="$result", value="Shows the result of the week", inline=False)
    embed.add_field(name="$update", value="Shows the update of the week", inline=False)
    embed.add_field(name="$kda", value="Shows the kda of the week", inline=False)
    embed.set_footer(text=random.choice(footer_text))
    await ctx.send(embed=embed)
    
    
@bot.command(name="update")
async def update(ctx):
    embed = discord.Embed(
        title="Update",
        description="The new attdance has appear ig",
        color= random.choice(color_codes)
    )
    embed.set_footer(text=random.choice(footer_text))
    await ctx.send(embed=embed)
    
@bot.command(name="kda")
async def kda(ctx):
    embed = discord.Embed(
        title="KDA",
        description="AVG kda this week",
        color= random.choice(color_codes)
    )
    file = discord.File("special spikey\kda_info.csv", filename="kda_info.csv")
    embed.set_footer(text=random.choice(footer_text))
    await ctx.send(embed=embed,file=file)

bot.run(os.getenv("TOKEN"))