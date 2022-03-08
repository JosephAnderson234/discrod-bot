import datetime

import discord
from discord.ext import commands
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='/', description='A bot for the Discord server')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def sum(ctx, n1: int, n2: int):
    await ctx.send(n1 + n2)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem impsun destague cadenset awaud", Timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

#event
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='with my code', url='https://www.twitch.tv/12jacr12'))
    print('we are ready to go!')


bot.run('OTM0MDk5NzI1OTkxNDQ0NTcy.YerKKQ.Y7L_zHa5-EsvMG9GuKDUBCrqnxc')