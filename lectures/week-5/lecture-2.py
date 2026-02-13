import pytest

'''
# Exercise 1

  Playlist
'''

class Playlist:
    __slots__: list[str] = ['name', '_songs']
    total_songs_added: int = 0
    
    def __init__(self, name: str, songs: list[str] | None = None):
        self.name: str = name
        self._songs: list[str] = songs if songs is not None else []

    @property
    def songs(self):
        return list(self._songs)

    def add_song(self, song: str):
        self._songs.append(song)
        Playlist.total_songs_added += 1

    @classmethod
    def get_total_songs_added(cls):
        return cls.total_songs_added
            
pl = Playlist("Chill")
pl.add_song("K.K. Cruisin")
pl.add_song("K.K. Folk")

print(pl.songs)                      # ["K.K. Cruisin", "K.K. Cruisin"]
pl.songs.append("Dont add!")         # Doesn't affect the playlist
print(len(pl.songs))                 # Still 2

print(Playlist.get_total_songs_added())  # 2

'''
# Exercise 2

  Validation
'''
