import discord 
intents = discord.Intents.default()
from discord.ext import commands


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