from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


class MediaCollection(ABC):
    """ABC for any collection that holds playable media."""

    @abstractmethod
    def add(self, item) -> None: ...

    @property
    @abstractmethod
    def total_duration(self) -> int: ...

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def __str__(self) -> str: ...
    

@dataclass
class Artist:
    """A musical artist."""

    name: str
    genre: str


class Listener:
    """A registered listener on the service."""

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def __str__(self):
        return f"Listener: {self.username}"

    def __repr__(self):
        return f"Listener({self.username!r}, {self.email!r})"


class Song:
    """A song available on the service."""

    def __init__(
        self,
        song_id: str,
        title: str,
        artist: Artist,
        duration: int = 210,
    ) -> None:
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration
        self._listeners: list[Listener] = []

    @property
    def artist(self) -> Artist:
        return self._artist

    @artist.setter
    def artist(self, art: Artist) -> None:
        if not isinstance(art, Artist):
            raise TypeError(
                "Only Artists can be credited on a song"
            )
        self._artist = art

    @property
    def listeners(self) -> list[Listener]:
        return self._listeners

    @listeners.setter
    def listeners(self, _) -> None:
        raise AttributeError(
            "Use stream() on a Playlist to add listeners"
        )

    def __str__(self):
        return f"{self.song_id}: {self.title}"

    def __len__(self):
        return len(self._listeners)


@dataclass
class StreamLog:
    """A record of a listener streaming a song."""

    listener: Listener
    song: Song
    streamed_at: datetime


class Playlist(MediaCollection):
    """A playlist managing songs and stream logs."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._songs: list[Song] = []
        self._streams: list[StreamLog] = []

    @property
    def songs(self) -> list[Song]:
        return self._songs

    def add(self, item) -> None:
        """Add a song to the playlist."""
        if not isinstance(item, Song):
            raise TypeError("Only Song objects can be added")
        self._songs.append(item)

    def stream(
        self, listener: Listener, song: Song, timestamp: datetime
    ) -> None:
        """Stream a song for a listener and log it."""
        if song not in self._songs:
            raise ValueError(
                f"{song.song_id} is not in {self.name}"
            )
        if listener in song._listeners:
            raise ValueError(
                f"{listener.username} already streamed {song.song_id}"
            )
        song._listeners.append(listener)
        self._streams.append(
            StreamLog(listener, song, timestamp)
        )

    @property
    def total_duration(self) -> int:
        return sum(s.duration for s in self._songs)

    @property
    def streams_by_date(self) -> dict[datetime, list[StreamLog]]:
        """Return stream logs grouped by date."""
        result: dict[datetime, list[StreamLog]] = {}
        for log in self._streams:
            if log.streamed_at not in result:
                result[log.streamed_at] = []
            result[log.streamed_at].append(log)
        return result

    def __str__(self) -> str:
        return f"{self.name} Playlist"

    def __len__(self) -> int:
        return len(self._songs)


chill_vibes = Playlist("Chill Vibes")

kk = Artist("K.K. Slider", "Acoustic")

isabelle = Listener("isabelle", "isabelle@townhall.ac")
tom_nook = Listener("tom_nook", "nook@nookinc.ac")
blathers = Listener("blathers", "blathers@museum.ac")

bubblegum = Song("KK-001", "K.K. Bubblegum", kk, 185)
cruisin = Song("KK-002", "K.K. Cruisin'", kk, 198)
stale_cupcakes = Song("KK-003", "Stale Cupcakes", kk, 210)

chill_vibes.add(bubblegum)
chill_vibes.add(cruisin)
chill_vibes.add(stale_cupcakes)

chill_vibes.stream(isabelle, bubblegum, datetime(2026, 2, 9))
chill_vibes.stream(tom_nook, bubblegum, datetime(2026, 2, 10))
chill_vibes.stream(isabelle, cruisin, datetime(2026, 2, 10))
chill_vibes.stream(blathers, stale_cupcakes, datetime(2026, 2, 10))

# List comprehension - get all song titles in playlist
titles = [song.title for song in chill_vibes.songs]

# Set comprehension - unique genres of artists
genres = {song.artist.genre for song in chill_vibes.songs}

# Dictionary comprehension - song_id to song title
song_dict = {song.song_id: song.title for song in chill_vibes.songs}

# Sort songs by duration (ascending)
sorted_songs = sorted(chill_vibes.songs, key=lambda s: s.duration)

# Sort songs by number of listeners (descending)
sorted_by_listeners = sorted(chill_vibes.songs, key=lambda s: len(s), reverse=True)

# Sort songs by title alphabetically
sorted_by_title = sorted(chill_vibes.songs, key=lambda s: s.title)

print("Start")
print(sorted_by_title)