#!/usr/bin/env python3

"""Trainer class for managing a team of Pokemon."""

from pokemon import Pokemon, FireType, WaterType


class Trainer:
    """A Pokemon trainer who manages a team of Pokemon."""

    def __init__(self, name: str) -> None:
        """Initialise a new Trainer."""
        self.max_team_size: int = 6
        self.name: str = name
        self.team: list[Pokemon] = []

    def add_to_team(self, pokemon: Pokemon) -> bool:
        """Add a Pokemon to the trainer's team.

        Returns True if successful, False if team is full.
        """

        if len(self.team) < self.max_team_size:
            self.team.append(pokemon)
            return True
        else:
            return False

    def get_team_size(self) -> int:
        """Get the number of Pokemon in the team."""
        return len(self.team)

    def get_first_available(self) -> Pokemon | None:
        """Get the first non-fainted Pokemon in the team."""
        for pokemon in self.team:
            if not pokemon.is_fainted():
                return pokemon
                
        return None

    def get_pokemon_by_type(self, pokemon_type: type) -> list[Pokemon]:
        """Get a list of all Pokemon in the team that are instances of pokemon_type."""
        return [pokemon for pokemon in self.team if isinstance(pokemon, pokemon_type)]

    def __str__(self) -> str:
        """Return a string representation of this Trainer."""
        return f"Trainer {self.name} has {self.get_team_size()} Pokemon."

ash = Trainer("Ash")

print(ash.get_pokemon_by_type(WaterType)) # Returns []

ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))

water_pokemon: list[Pokemon] = ash.get_pokemon_by_type(WaterType)  # Returns [Squirtle]
print(water_pokemon[0].name)

fire_pokemon: list[Pokemon] = ash.get_pokemon_by_type(FireType)  # Returns [Charmander]
print(fire_pokemon[0].name)

ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))

fire_pokemon: list[Pokemon] = ash.get_pokemon_by_type(FireType)  # Returns [Charmander, Charmander]
print(fire_pokemon)