import discord
from discord.ext import commands
import Data_Processing

bot = commands.Bot(command_prefix= "!", intents= discord.Intents.all())

@bot.command()
async def info(ctx, champ, lane):
    res, chmp = Data_Processing.get_champ(champ.lower(), lane.lower())
    if res:
        await ctx.send(f"""{lane} {champ} is currently a meta pick. Playing is the right choice. {lane} {champ} is good against:
                       {chmp.good_against} 

And also if you are feeling comfortable with {lane} {champ} following matchups are skill based: 
                       {chmp.playable} 

You can build {chmp.build} 

But if your opponent choose it you still have so many choices like: 
                       {chmp.counters}""")
    else:
        await ctx.send(chmp)
@bot.command()
async def helpp(ctx):
    await ctx.send("Welcome to the Lol Pickmaker Bot. I am here to improve your gaming experience and assist you during the ban selection screen. Currently, I'm in the beta version and can only help you with providing builds and counters for champions in their usual lanes. To use this command, you can type !info {champion name} {lane} in the chat.")

