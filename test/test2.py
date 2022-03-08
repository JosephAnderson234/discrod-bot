import discord
from discord.utils import get
from discord.ext import commands
import os
import youtube_dl

client = commands.Bot(command_prefix="!")

@client.command()
async def conectar(ctx):
    canal = ctx.message.author.voice.channel
    if not canal:
        await ctx.send("No estas conectado a un canal de voz")
        return
    voz = get(client.voice_clients, guild=ctx.guild)
    if voz and voz.is_connected():
        await voz.move_to(canal)
    else:
        voz = await canal.connect()
client.run('OTM0MDk5NzI1OTkxNDQ0NTcy.YerKKQ.Y7L_zHa5-EsvMG9GuKDUBCrqnxc')