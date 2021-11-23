from pytube import YouTube
from moviepy.editor import * 

class Downloader:
    def __init__(self):
        pass

    def download(self, url):
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()
        title = ys.title
        print(f'Ah! {title}! A good choice.')
        song = ys.download('musikk')
        self.convert(song, title)
        print(f'{title} is now downloaded.')
        return title
    
    def convert(self, song, title):
        while True:
            try:
                mp4_file = song
                mp3_file = os.rename(mp4_file, f'musikk/{title}.mp3')

                videoclip = VideoFileClip(mp4_file)
                audioclip = videoclip.audio
                audioclip.write_audiofile(mp3_file)
                audioclip.close()
                videoclip.close()
            except:
                print('Video converted to playable music.')
            break
        

fil = ('https://www.youtube.com/watch?v=XD0hUkE__ps')
