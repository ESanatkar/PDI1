import copy
from abc import ABC, abstractmethod
from datetime import datetime
import random

'''
# Exercise 1

  Playlist Sorting
'''

class Song:
    def __init__(self, title: str, artist: str, rating: float):
        self.title: str = title
        self.artist: str = artist
        self.rating: int | float = rating

    def __repr__(self):
        return f"{self.title} - {self.artist} (rating: {self.rating})"

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, songs: list[Song]) -> list[Song]:
        pass
        
class SortByTitle(SortStrategy):
    def sort(self, songs: list[Song]) -> list[Song]:
        return sorted(songs, key=lambda s: s.title)

class SortByRating(SortStrategy):
    def sort(self, songs: list[Song]) -> list[Song]:
        return sorted(songs, key=lambda s: s.rating, reverse=True)
        
class ShuffleSort(SortStrategy):
    def sort(self, songs: list[Song]) -> list[Song]:
        shuffled: list[Song] = copy.deepcopy(songs)
        random.shuffle(shuffled)
        return shuffled
    
class Playlist:
    def __init__(self, name: str, strategy: SortStrategy):
        self.name: str = name
        self.strategy: SortStrategy = strategy
        self.songs: list[Song] = []

    def add(self, song: Song) -> None:
        self.songs.append(song)
        print(f"Added {song.title}, {song.artist} to {self.name} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")

    def sort(self) -> None:
        self.songs: list[Song] = self.strategy.sort(self.songs)

    def display(self) -> None:
        print(f"Playlist: {self.name}")
        for i, song in enumerate(self.songs, 1):
            print(f"  {i}. {song}")
            
playlist = Playlist("Island Tunes", SortByTitle())

playlist.add(Song("K.K. Bossa", "K.K. Slider", 4.5))
playlist.add(Song("Bubblegum K.K.", "K.K. Slider", 4.9))
playlist.add(Song("K.K. Cruisin'", "K.K. Slider", 4.2))
playlist.add(Song("Stale Cupcakes", "K.K. Slider", 4.7))
playlist.add(Song("K.K. Disco", "K.K. Slider", 3.8))

# Sort and display the playlist
playlist.sort()
playlist.display() 

# Change sort strategy to SortByRating
playlist.strategy = SortByRating()
playlist.sort()
playlist.display()

# Change sort strategy to ShuffleSort
playlist.strategy = ShuffleSort()
playlist.sort()
playlist.display()