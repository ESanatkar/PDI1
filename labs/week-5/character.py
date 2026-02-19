from abc import ABC, abstractmethod
from exceptions import InvalidLivesError, InvalidCoinsError, CharacterDeadError

class Character(ABC):
    total_characters = 0

    def __init__(self, name: str, lives: int =3, speed: float =1.0) -> None:
        self._name: str = name
        self.lives: int = lives
        self._coins = 0
        self._speed: int | float = speed
        Character.total_characters += 1

    @property
    def name(self):
        return self._name

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        if not isinstance(value, int):
            raise TypeError("Lives must be an integer")
        if not (0 <= value <= 99):
            raise InvalidLivesError()
        self._lives = value

    @property
    def coins(self):
        return self._coins

    @coins.setter
    def coins(self, value):
        if not isinstance(value, int):
            raise TypeError("Coins must be an integer")
        if not (0 <= value <= 999):
            raise InvalidCoinsError()
        self._coins = value

    @property
    def is_alive(self):
        return self._lives > 0

    def collect_coin(self):
        self._coins += 1
        if self._coins >= 100:
            self._coins = 0
            self._lives = min(self._lives + 1, 99)
            return f"{self._name} collected 100 coins and gained a life! Lives: {self._lives}"
        return f"{self._name} collected a coin! Coins: {self._coins}"

    def take_damage(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        self._lives -= 1
        if not self.is_alive:
            return f"{self._name} lost a life and is now dead! Lives: {self._lives}"
        return f"{self._name} lost a life! Lives: {self._lives}"

    @classmethod
    def get_total_characters(cls):
        return cls.total_characters


class Mario(Character):
    def __init__(self, lives=3):
        super().__init__(name="Mario", lives=lives, speed=1.0)

    def jump(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Mario jumps!"

    def run(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Mario runs at normal speed!"

    def special_ability(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Mario uses fireball!"


class Luigi(Character):
    def __init__(self, lives=3):
        super().__init__(name="Luigi", lives=lives, speed=0.9)

    def jump(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Luigi jumps higher and floatier!"

    def run(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Luigi runs with slippery momentum!"

    def special_ability(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Luigi uses Poltergust!"


class Peach(Character):
    def __init__(self, lives=3):
        super().__init__(name="Peach", lives=lives, speed=0.85)

    def jump(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Peach floats gracefully through the air!"

    def run(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Peach runs elegantly!"

    def special_ability(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Peach uses her parasol!"


class Toad(Character):
    def __init__(self, lives=3):
        super().__init__(name="Toad", lives=lives, speed=1.2)

    def jump(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Toad does a short but quick jump!"

    def run(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Toad zooms ahead!"

    def special_ability(self):
        if not self.is_alive:
            raise CharacterDeadError(self._name)
        return "Toad uses spore burst!"