from pytube import YouTube
from typer import Typer
import os


app = Typer()


@app.command()
def download_360p_mp4_videos(url: str, outpath: str = "./"):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path='./outputs/')

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


if __name__ == "__main__":
    app()
