from pytube import YouTube
from typer import Typer
import os

app = Typer()


@app.command()
def download_musics():
    with open("musics.txt") as file:
        for line in file:
            youtube = YouTube(line)
            music = youtube.streams.filter(only_audio=True).first()

            out_file = music.download(output_path='./outputs/')

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)


if __name__ == "__main__":
    app()
