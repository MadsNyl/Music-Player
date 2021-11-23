import os, vlc

class Playlist:
    def __init__(self, name):
        self.name = name
        self.playlist = []
    
    def store_music(self):
        self.playlist = []
        songs = os.listdir('musikk')
        for song in songs:
            self.playlist.append(song)
    
    def show_music(self):
        for index, song in enumerate(self.playlist):
            print(index, song)
            print('.' * 10)
    
    def play_music(self, song_index):
        for index, song in enumerate(self.playlist):
            if index == int(song_index):
                player = vlc.MediaPlayer(f'musikk/{song}')
                player.play() 
                run = True
                while run:
                    user_input = input('Pause: "pause".\nReplay: "play":\nNew song: "new": ')
                    if user_input == 'pause':
                        player.pause()
                    elif user_input == 'play':
                        player.play()
                    elif user_input == 'new':
                        player.stop()
                        run = False
            