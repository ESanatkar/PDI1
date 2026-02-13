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

class Thermostat:
    def __init__(self, temperature=20):
        self.temperature = temperature
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        value = max(10, min(35, value))
        self._temperature = round(value * 2) / 2

t = Thermostat(22)
t.temperature = 8
print(t.temperature)   # 10.0

t.temperature = 23.3
print(t.temperature)   # 23.5

'''
# Exercise 3

  Static & Class Variables
'''

class Player:
    player_count = 0
    
    def __init__(self, name, score=0):
        if not Player.is_valid_name(name):
            raise ValueError("Must be a non-empty string with no more than 20 characters")
        self.name = name
        self.score = score
        Player.player_count += 1
    
    @classmethod
    def get_player_count(cls):
        return cls.player_count
    
    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and 0 < len(name) <= 20

p1 = Player("Mario")
p2 = Player("Waluigi")
print(Player.get_player_count())     # 2
print(Player.is_valid_name(""))      # False