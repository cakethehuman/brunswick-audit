import discord
import random
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

class formating:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        
    def command_maker(self):
        return discord.Embed(title= self.title,
                             description= self.description, 
                             color= random.choice(color_codes),
                             )
    def test(self):
        print("test" + self.title + self.description)
        