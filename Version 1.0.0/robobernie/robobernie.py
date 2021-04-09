from btlmet import NAresort, EUresort, terri, HellLetLoose
import discord
from discord.ext import commands

TOKEN = "REDACTED"

description = '''The offical Discord Bot of Bernies Resort!'''
bot = commands.Bot(command_prefix='??', description=description)



@bot.command()
async def NAResort(ctx):
    ServName = NAresort()[0]
    Map = NAresort()[1]
    Status = NAresort()[2]
    ip = str(NAresort()[3])
    playerCount = NAresort()[4]
    rank = str(NAresort()[5])
    NAmsg = (">>> **" + ServName +"**\n\n:map: Map: "+Map+"\n:red_circle: Status: "+Status+"\n:globe_with_meridians: IP: "+ip+"\n:man_standing: Player Count: "+playerCount+"\n:medal: Server Rank: "+ rank)
    await ctx.send(NAmsg, file=discord.File('images/NA.png'))

@bot.command()
async def EUResort(ctx):
    ServName = EUresort()[0]
    Map = EUresort()[1]
    Status = EUresort()[2]
    ip = str(EUresort()[3])
    playerCount = EUresort()[4]
    rank = str(EUresort()[5])
    NAmsg = (">>> **" + ServName +"**\n\n:map: Map: "+Map+"\n:red_circle: Status: "+Status+"\n:globe_with_meridians: IP: "+ip+"\n:man_standing: Player Count: "+playerCount+"\n:medal: Server Rank: "+ rank)
    await ctx.send(NAmsg, file=discord.File('images/EU.png'))

@bot.command()
async def TE(ctx):
    ServName = terri()[0]
    Map = terri()[1]
    Status = terri()[2]
    ip = str(terri()[3])
    playerCount = terri()[4]
    rank = str(terri()[5])
    NAmsg = (">>> **" + ServName +"**\n\n:map: Map: "+Map+"\n:red_circle: Status: "+Status+"\n:globe_with_meridians: IP: "+ip+"\n:man_standing: Player Count: "+playerCount+"\n:medal: Server Rank: "+ rank)
    await ctx.send(NAmsg, file=discord.File('images/Ter.png'))

@bot.command()
async def HLL(ctx):
    ServName = HellLetLoose()[0]
    Map = HellLetLoose()[1]
    Status = HellLetLoose()[2]
    ip = str(HellLetLoose()[3])
    playerCount = HellLetLoose()[4]
    rank = str(HellLetLoose()[5])
    NAmsg = (">>> **" + ServName +"**\n\n:map: Map: "+Map+"\n:red_circle: Status: "+Status+"\n:globe_with_meridians: IP: "+ip+"\n:man_standing: Player Count: "+playerCount+"\n:medal: Server Rank: "+ rank)
    await ctx.send(NAmsg, file=discord.File('images/HLL.png'))
bot.run(TOKEN)
