import youtube_dl
import os

song_there = os.path.isfile("song.mp3")
try:
    if song_there:
        os.remove("song.mp3")
except PermissionError:
    print("Wait for the current playing music to end or use the 'stop' command")

ydl_opts = {
        'format': 'bestaudio/best',
        #'postprocessors': [{
        #    'key': 'FFmpegExtractAudio',
        #    'preferredcodec': 'mp3',
        #    'preferredquality': '192',
        #}],
    }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://youtu.be/ktvTqknDobU"])
    for file in os.listdir("./"):
        if file.endswith(".m4a"):
            os.rename(file, "song.mp3")