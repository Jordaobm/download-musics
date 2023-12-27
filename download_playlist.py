import os
import re
from pytube import Playlist, YouTube
from typer import Typer
from moviepy.editor import AudioFileClip

app = Typer()

def clean_playlist_name(name):
    # Substituir caracteres especiais por letras
    clean_name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
    # Substituir espaços por underline
    clean_name = clean_name.replace(' ', '_')
    return clean_name

@app.command()
def get_playlist():
    with open("download_playlist.txt") as file:
        for line in file:
            # Retrieve URLs of videos from playlist
            playlist = Playlist(line)

            for url in playlist:
                download_musics(url, clean_playlist_name(playlist.title))


def convert_to_mp3(input_file, output_file):
    audio = AudioFileClip(input_file)
    audio.write_audiofile(output_file)
    audio.close()


def download_musics(url, name):
    youtube = YouTube(url)
    music = youtube.streams.filter(only_audio=True).first()

    out_file = music.download(output_path=f'./outputs/{name}')

    base, ext = os.path.splitext(out_file)
    new_file = f'{base}.mp3'

    convert_to_mp3(out_file, new_file)

    os.remove(out_file)  # Remove o arquivo webm original se desejar economizar espaço


if __name__ == "__main__":
    app()
