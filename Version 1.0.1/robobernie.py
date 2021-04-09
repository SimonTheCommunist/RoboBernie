from btlmet import NAresort, EUresort, terri, HellLetLoose
from Rs2graph import terriGraph, NAResortGraph, EUResortGraph, HLLGraph
import discord
from discord.ext import commands

TOKEN = "REDACTED"

description = '''The offical Discord Bot of Bernies Resort!'''
bot = commands.Bot(command_prefix='??', description=description)

@bot.command()
async def NAResort(ctx):
    NAResortGraph()
    file = discord.File("images/NA.png")
    ServName = NAresort()[0]
    Map = NAresort()[1]
    Status = NAresort()[2]
    ip = str(NAresort()[3])
    playerCount = NAresort()[4]
    rank = str(NAresort()[5])
    embed=discord.Embed(title=ServName, description="\n\n:map: Map: "+Map+"\n:red_circle: Status: "+Status+"\n:globe_with_meridians: IP: "+ip+"\n:man_standing: Player Count: "+playerCount+"\n:medal: Server Rank: "+ rank, color=discord.Color.blue())
    embed.set_image(url="attachment://NA.png")
    await ctx.send(embed=embed, file=file)

@bot.command()
async def EUResort(ctx):
    NAResortGraph()
    file = discord.File("images/EU.png")
    ServName = EUresort()[0]
    Map = EUresort()[1]
    Status = NAresort()[2]
    ip = str(NAresort()[3])
    playerCount = NAresort()[4]
    rank = str(NAresort()[5])
    embed=discord.Embed(title=ServName, description="\n\n:map: Map: "+Map+"\n:red_circle: Status: "+Status+"\n:globe_with_meridians: IP: "+ip+"\n:man_standing: Player Count: "+playerCount+"\n:medal: Server Rank: "+ rank, color=discord.Color.blue())
    embed.set_image(url="attachment://EU.png")
    await ctx.send(embed=embed, file=file)

@bot.command()
async def TE(ctx):
    NAResortGraph()
    file = discord.File("images/Ter.png")
    ServName = terri()[0]
    Map = terri()[1]
    Status = terri()[2]
    ip = str(terri()[3])
    playerCount = terri()[4]
    rank = str(terri()[5])
    embed=discord.Embed(title=ServName, description="\n\n:map: Map: "+Map+"\n:red_circle: Status: "+Status+"\n:globe_with_meridians: IP: "+ip+"\n:man_standing: Player Count: "+playerCount+"\n:medal: Server Rank: "+ rank, color=discord.Color.blue())
    embed.set_image(url="attachment://Ter.png")
    await ctx.send(embed=embed, file=file)

@bot.command()
async def HLL(ctx):
    NAResortGraph()
    file = discord.File("images/HLL.png")
    ServName = HellLetLoose()[0]
    Map = HellLetLoose()[1]
    Status = HellLetLoose()[2]
    ip = str(HellLetLoose()[3])
    playerCount = HellLetLoose()[4]
    rank = str(HellLetLoose()[5])
    embed=discord.Embed(title=ServName, description="\n\n:map: Map: "+Map+"\n:red_circle: Status: "+Status+"\n:globe_with_meridians: IP: "+ip+"\n:man_standing: Player Count: "+playerCount+"\n:medal: Server Rank: "+ rank, color=discord.Color.blue())
    embed.set_image(url="attachment://HLL.png")
    await ctx.send(embed=embed, file=file)

bot.run(TOKEN)