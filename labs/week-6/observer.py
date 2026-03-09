from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from decorator import log_spawn

Rarity = Literal["common", "uncommon", "rare"]


@dataclass
class Spawn:
    name: str
    cp: int
    rarity: Rarity
    distance_km: float


class Observer(ABC):
    @abstractmethod
    def update(self, spawn: Spawn) -> None:
        ...


class SpawnPoint:
    """Subject that records nearby Pokémon spawns and notifies observers."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._observers: list[Observer] = []
        self._spawns: list[Spawn] = []

    def subscribe(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def spawn(self, name: str, cp: int, rarity: Rarity, distance_km: float) -> None:
        new_spawn = Spawn(name=name, cp=cp, rarity=rarity, distance_km=distance_km)
        self._spawns.append(new_spawn)
        for observer in self._observers:
            observer.update(new_spawn)

    def get_all(self) -> list[Spawn]:
        return self._spawns


class PlayerAlert(Observer):
    """Notifies a named player whenever any Pokémon spawns nearby."""

    def __init__(self, player_name: str) -> None:
        self.player_name: str = player_name

    def update(self, spawn: Spawn) -> None:
        print(f"[Alert] {self.player_name}: {spawn.name} appeared {spawn.distance_km}km away (CP {spawn.cp})")


class RareBroadcast(Observer):
    """Broadcasts a message when a rare Pokémon spawns."""

    def update(self, spawn: Spawn) -> None:
        if spawn.rarity == "rare":
            print(f"[Rare spawn] {spawn.name} appeared {spawn.distance_km}km away (CP {spawn.cp})")