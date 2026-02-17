from abc import ABC, abstractmethod

'''
# Exercise 2

  Playlist Advanced
'''

class Song:
    def __init__(self, title: str, artist: str):
        self.title: str = title
        self.artist: str = artist

    def __str__(self) -> str:
        return f'"{self.title}" by {self.artist}'


class PlaylistObserver(ABC):
    """Abstract base class for anything that wants to observe a playlist."""

    @abstractmethod
    def notify(self, playlist_name: str, song: Song) -> None:
        """Notify the observer when a song is added to the playlist."""
        print(f"Observer notified: {song} added to {playlist_name}")

class ObservablePlaylist:
    """A playlist that notifies observers when songs are added."""

    def __init__(self, name: str):
        self.name = name
        self._songs: list[Song] = []
        self._observers: list[PlaylistObserver] = []

    def subscribe(self, observer: PlaylistObserver) -> None:
        """Add an observer to the notification list."""
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: PlaylistObserver) -> None:
        """Remove an observer from the notification list."""
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify_all(self, song: Song) -> None:
        """Notify all observers that a song was added."""
        for observer in self._observers:
            observer.notify(self.name, song)

    def add_song(self, song: Song) -> None:
        """Add a song to the playlist and notify observers."""
        self._songs.append(song)
        self._notify_all(song)

'''
# Exercise 1

  User Class
'''

class User(PlaylistObserver):
    def __init__(self, username: str):
        self.username: str = username

    def notify(self, playlist_name: str, song: Song) -> None:
        print(f"[{self.username}] \"{song.title}\" by {song.artist} was added to {playlist_name}")

'''
# Exercise 3

  Playlist Implementation
'''