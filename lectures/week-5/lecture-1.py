from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Union, overload

'''
# Exercise 1


  Media Class
'''

class Song:
    def __init__(self, title: str, artist: str):
        self.title: str = title
        self.artist: str = artist
        self.played = False
    
    def play(self):
        self.played = True
        print(f"Now playing: {self.title}")

class MediaCollection(ABC):
    def __init__(self, name: str):
        self.name: str = name
        self.songs: list[Song] = []

    @abstractmethod
    def add(self, song: Song) -> None:
        """Add a song to the collection."""
        pass

    def play_all(self) -> None:
        for song in self.songs:
            song.play()


class Playlist(MediaCollection, Sequence):
    def add(self, song: Song) -> None:
        self.songs.append(song)

    @overload
    def __getitem__(self, index: int) -> Song: ...
    
    @overload
    def __getitem__(self, index: slice) -> Sequence[Song]: ...
    
    def __getitem__(self, index: Union[int, slice]) -> Union[Song, Sequence[Song]]:
        return self.songs[index]

    def __len__(self) -> int:
        return len(self.songs)

class Album(MediaCollection):
    def __init__(self, name: str, max_tracks: int):
        super().__init__(name)
        self.max_tracks: int = max_tracks

    def add(self, song: Song) -> None:
        if len(self.songs) >= self.max_tracks:
            raise ValueError(
                f"Album '{self.name}' cannot have more than {self.max_tracks} tracks."
            )
        self.songs.append(song)

p = Playlist("Playlist Track")
s1 = Song("A", "Artist")
s2 = Song("B", "Artist")

p.add(s1)
p.add(s2)

for s in p:
    print(s.title)

print(s1 in p)   # True
print(p.count(s1))  # 1
print(p.index(s2))  # 1
