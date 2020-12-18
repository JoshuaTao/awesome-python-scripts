import youtube_dl
import os

os.chdir("----enter a directory path to store downloaded videos----")
ydl_opts = {
    "format": "bestvideo[ext=webm]+bestaudio[ext=webm]/best",
    "outtmpl": "%(title)s.%(ext)s",
}

url = input("What's the url?\n")

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
