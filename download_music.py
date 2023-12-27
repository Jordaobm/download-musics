from pytube import YouTube
from typer import Typer
import os
from moviepy.editor import AudioFileClip

app = Typer()


def convert_to_mp3(input_file, output_file):
    audio = AudioFileClip(input_file)
    audio.write_audiofile(output_file)
    audio.close()


@app.command()
def download_musics():
    with open("download_music.txt") as file:
        for line in file:
            try:
                youtube = YouTube(line)
                music = youtube.streams.filter(only_audio=True).first()

                out_file = music.download(output_path='./outputs/')

                base, ext = os.path.splitext(out_file)
                new_file = f'{base}.mp3'

                convert_to_mp3(out_file, new_file)

                os.remove(out_file)  # Remove o arquivo webm original se desejar economizar espaço
            except:
                print(f"O vídeo {line} possui restrição de idade. Pulando para o próximo vídeo.")
                return


if __name__ == "__main__":
    app()
