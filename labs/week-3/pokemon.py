#!/usr/bin/env python3

"""Pokemon classes for the battle system."""

import random


class Pokemon:
    """Base class for all Pokemon."""

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defence: int,
        move: str,
        move_power: int,
    ) -> None:
        """Initialise a new Pokemon."""
        self.name: str = name
        self.max_hp: int = max_hp
        self.current_hp: int = max_hp
        self.attack: int = attack
        self.defence: int = defence
        self.move: str = move
        self.move_power: int = move_power

    def take_damage(self, amount: int) -> None:
        """Reduce current_hp by amount (minimum 0)."""
        self.current_hp: int = max(0, self.current_hp - amount)

    def calculate_damage(self, defender: "Pokemon") -> int:
        """Calculate damage dealt to defender.

        Damage is a random value between 85% and 100% of max damage.
        Minimum damage is 1.
        """
        max_damage = int((self.attack / defender.defence) * self.move_power)
        min_damage = int(max_damage * 0.85)
        return max(1, random.randint(min_damage, max_damage))

    def is_fainted(self) -> bool:
        """Check if the Pokemon has fainted."""
        fainted: bool = True and self.current_hp <= 0 or False
        return fainted

    def attack_move(self) -> str:
        """Return the attack message for this Pokemon."""
        
        return f"{self.name} uses {self.move} !"

    def description(self) -> str:
        """Return a description of this Pokemon."""
        return f"{self.name} is a {self.__class__.__name__} type."

    def __str__(self) -> str:
        """Return a string representation of this Pokemon."""
        return f"{self.name} (HP: {self.current_hp}/{self.max_hp})"

class FireType(Pokemon):
    """A Fire type Pokemon."""

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defence: int,
        move: str,
        move_power: int,
        burn_chance: float,
    ) -> None:
        """Initialise a new Fire type Pokemon."""
        self.name: str = name
        self.max_hp: int = max_hp
        self.current_hp: int = max_hp
        self.attack: int = attack
        self.defence: int = defence
        self.move: str = move
        self.move_power: int = move_power
        self.burn_chance: float = burn_chance

    def description(self) -> str:
        """Return a description of this Fire type Pokemon."""
        return f"{self.name} is a Fire type Pokemon with a {self.burn_chance * 100}% chance to burn with attacks."

class WaterType(Pokemon):
    """A Water type Pokemon."""

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defence: int,
        move: str,
        move_power: int,
        swim_speed: int,
    ) -> None:
        """Initialise a new Water type Pokemon."""
        self.name: str = name
        self.max_hp: int = max_hp
        self.current_hp: int = max_hp
        self.attack: int = attack
        self.defence: int = defence
        self.move: str = move
        self.move_power: int = move_power
        self.swim_speed: int = swim_speed

    def description(self) -> str:
        """Return a description of this Water type Pokemon."""
        return f"{self.name} is a Water type Pokemon with a swim speed of {self.swim_speed}."