from youtube_dl import YoutubeDL
from pydub import AudioSegment
from predicter import eval
import os

audio_downloader = YoutubeDL({'format': 'bestaudio'})

try:
    print('Youtube Downloader'.center(40, '_'))
    URL = input('Enter youtube URL :  ')
    info = audio_downloader.extract_info(URL)
    filename = info['title'] + '-' + info['id'] + '.' + info['container'].split('_')[0]
except Exception:
    print("Couldn\'t download the audio")

finally:
    #sound = AudioSegment.from_file(filename)
    #filename = filename + '.mp3'
    #sound.export(filename, format="mp3")

    path = os.getcwd() + "\\" + filename
    eval(path)
