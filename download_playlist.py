import os

from pytube import Playlist, YouTube
from typer import Typer

app = Typer()


@app.command()
def get_playlist():
    with open("download_playlist.txt") as file:
        for line in file:
            # Retrieve URLs of videos from playlist
            playlist = Playlist(line)

            for url in playlist:
                download_musics(url, playlist.title)
            



def download_musics(url, name):
    youtube = YouTube(url)
    music = youtube.streams.filter(only_audio=True).first()

    out_file = music.download(output_path='./outputs/' + name)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
            



if __name__ == "__main__":
    app()
