import discord
import random
from .utils import color_codes

class Format:
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
        