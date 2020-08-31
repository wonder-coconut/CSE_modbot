import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!')
bot.remove_command('help') 

def getToken():
    tokenFile = open('TOKEN.txt','r')
    tokentxt = tokenFile.read()
    return tokentxt

@bot.event
async def on_ready():
    print('logged in as '+str(bot.user))

@bot.command(name = "join-batch1")
async def batch1(ctx):
    server = ctx.guild
    await server.create_role(name="Bitchboy",colour=discord.Colour(0x00FFFF))
    user = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name = "Batch 1")
    await user.add_roles(role)

@bot.command(name = "join-batch2")
async def batch2(ctx):
    server = ctx.guild
    await server.create_role(name="Bitchboy",colour=discord.Colour(0x00FFFF))
    user = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name = "Batch 2")
    await user.add_roles(role)

bot.run (getToken())