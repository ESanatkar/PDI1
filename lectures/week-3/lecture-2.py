'''
# Exercise 1


  Set Classes
'''

class Pokemon:
    def __init__(self, name: str, max_hp: int) -> None:
        self.name: str = name
        self.max_hp: int = max_hp
        self.current_hp: int = max_hp

    def description(self) -> str:
        return f"{self.name} is a Normal type"

class FireType(Pokemon):
    def __init__(self, name: str, max_hp: int, burn_chance: float) -> None:
        super().__init__(name, max_hp)
        self.current_hp: int = max_hp
        self.burn_chance: float = burn_chance

    def description(self) -> str:
        return f"{self.name} is a Fire type"

class WaterType(Pokemon):
    def __init__(self, name: str, max_hp: int, swim_speed: int) -> None:
        super().__init__(name, max_hp)
        self.current_hp: int = max_hp
        self.swim_speed: int = swim_speed

    def description(self) -> str:
        return f"{self.name} is a Water Type"


charmander = FireType("Charmander", 39, 0.2)
print(charmander.name)        # Charmander
print(charmander.current_hp)  # 39 (inherited)
print(charmander.burn_chance) # 0.2
print(charmander.description())  # Charmander is a Fire type


squirtle = WaterType("Squirtle", 44, 5)
print(squirtle.swim_speed)     # 5
print(squirtle.description())  # Squirtle is a Water type