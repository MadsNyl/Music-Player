from downloader import Downloader
from playlist import Playlist
import os

def seperate_text():
    print('.' * 10)

print('Welcome to your personal music app')
playlist_name = input('Let us start with creating your playlist.\nPlease type a name for your playlist: ')
playlist = Playlist(playlist_name)
downloader = Downloader()
seperate_text()

run_app = True
while run_app:
    
    user_input = input(f'Great! Now to add some songs to "{playlist_name}", type "add".\nTo show your music, type "show".\nTo store your music to your playlist, type "store":\nTo play music, type "play":\nTo close your app, type "close": ')

    seperate_text()

    if user_input == 'add':
        user_input = input('Please copy/paste a YouTube URL to download music: ')
        downloader.download(user_input)
        seperate_text()
    elif user_input == 'show':
        playlist.show_music()
        seperate_text()
    elif user_input == 'store':
        playlist.store_music()
        print(f'Your music is now stored in "{playlist_name}"')
        seperate_text()
    elif user_input == 'play':
        playlist.show_music()
        index = input('Type in a song to play. It must be identic to the name: ')
        playlist.play_music(index)
        seperate_text()
    elif user_input == 'close':
        print('Good Bye!')
        run_app = False

    



