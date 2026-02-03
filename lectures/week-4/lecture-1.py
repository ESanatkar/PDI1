import random
from math import prod
import time

'''
# Exercise 1


  Playlist
'''

class Song:
    def __init__(self, title: str, artist: str):
        self.title: str = title
        self.artist: str = artist
        self.played = False
    
    def play(self):
        self.played = True
        print(f"Now playing: {self.title}")

class Playlist: 
    def __init__(self, name: str):
        self.name: str = name
        self.songs: list[Song] = []
    
    def add_song(self, song: Song) -> None:
        self.songs.append(song)
    
    def __getitem__(self, index: int) -> Song:
        return self.songs[index]
    
    def __len__(self) -> int:
        return len(self.songs)

    def __iter__(self):
        for song in self.songs:
            yield song

    def __contains__(self, song: Song) -> bool:
        return song in self.songs
    
    def __bool__(self) -> bool:
        return any(song.played for song in self.songs)

playlist = Playlist("New Albums")
playlist.add_song(Song("Track 1", "Artist A"))
playlist.add_song(Song("Track 2", "Artist B"))

print(bool(playlist))  # Should print: False (nothing played yet)

playlist[0].play()     # Now playing: Track 1
print(bool(playlist))  # Should print: True