#!/usr/bin/env python3


class Item:
    """A collectible item in the game."""

    def __init__(self, name: str, value: int, quantity: int = 1) -> None:
        self.name = name
        self.value = value
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Item('{self.name}', value={self.value}, qty={self.quantity})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Item):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


class Weapon:
    """A weapon that can be equipped."""

    def __init__(self, name: str, damage: int, durability: int = 100) -> None:
        self.name = name
        self.damage = damage
        self.durability = durability

    def attack(self) -> str:
        """Perform an attack with this weapon."""
        if self.durability <= 0:
            return f"{self.name} is broken!"
        self.durability -= 10
        return f"Attacked with {self.name} for {self.damage} damage!"

    def __repr__(self) -> str:
        return f"Weapon('{self.name}', dmg={self.damage}, dur={self.durability})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Weapon):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


class Enemy:
    """An enemy that Link can encounter."""

    def __init__(self, name: str, health: int, strength: int) -> None:
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self) -> str:
        """Enemy performs an attack."""
        return f"{self.name} attacks for {self.strength} damage!"

    def __repr__(self) -> str:
        return f"Enemy('{self.name}', hp={self.health}, str={self.strength})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Enemy):
            return False
        return self.name == other.name

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Enemy):
            return NotImplemented
        return self.strength < other.strength


class Inventory:
    """Link's inventory."""

    def __init__(self) -> None:
        self._items: list[Item] = []

    def add_item(self, item: Item) -> None:
        """Add an item to the inventory."""
        self._items.append(item)

    def __getitem__(self, key: int | slice) -> Item | list[Item]:
        return self._items[key]

    def __setitem__(self, key: int, value: Item) -> None:
        self._items[key] = value

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def iter_valuable(self, min_value: int):
        for item in self._items:
            if item.value >= min_value:
                yield item

    def __contains__(self, item: object) -> bool:
        if isinstance(item, str):
            return any(i.name == item for i in self._items)
        if isinstance(item, Item):
            return any(i == item for i in self._items)
        return False


class Dungeon:
    """A dungeon containing rooms."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._rooms: list["Room"] = []

    def add_room(self, room: "Room") -> None:
        """Add a room to the dungeon."""
        self._rooms.append(room)

    def __getitem__(self, key: int | slice) -> "Room" | list["Room"]:
        return self._rooms[key]

    def __len__(self) -> int:
        return len(self._rooms)

    def __iter__(self):
        for room in self._rooms:
            yield room

    def __contains__(self, item: object) -> bool:
        if isinstance(item, str):
            return any(r.name == item for r in self._rooms)
        if isinstance(item, Room):
            return any(r.name == item.name for r in self._rooms)
        return False

    def iter_uncleared(self):
        for room in self._rooms:
            if not room.cleared:
                yield room


class Room:
    """A room in a dungeon."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._enemies: list[Enemy] = []
        self._items: list[Item] = []
        self.cleared = False

    def __repr__(self) -> str:
        return (
            f"Room('{self.name}', enemies={len(self._enemies)}, cleared={self.cleared})"
        )

    def add_enemy(self, enemy: Enemy) -> None:
        """Add an enemy to the room."""
        self._enemies.append(enemy)

    def add_item(self, item: Item) -> None:
        """Add an item to the room."""
        self._items.append(item)

    def __bool__(self) -> bool:
        return len(self._enemies) > 0 and not self.cleared


if __name__ == "__main__":
    print("Zelda Protocols!")