from  nicegui import ui
from Functions import universalFunctions
from pytube import YouTube
import os
def downlaodMusic(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    ui.download(new_file)