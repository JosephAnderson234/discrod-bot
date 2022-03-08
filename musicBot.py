import pytest
from discord.utils import get
import discord
from discord.ext import commands
import os
import youtube_dl

client = commands.Bot(command_prefix="!")

voiceChannel = discord.VoiceChannel(762740714319904821)
voiceChannel.connect()

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='music')
    #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voiceChannel.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voiceChannel.is_connected():
        await voiceChannel.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voiceChannel = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voiceChannel.is_playing():
        voiceChannel.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voiceChannel = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voiceChannel.is_paused():
        voiceChannel.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voiceChannel = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voiceChannel.stop()
client.run('OTM0MDk5NzI1OTkxNDQ0NTcy.YerKKQ.Y7L_zHa5-EsvMG9GuKDUBCrqnxc')