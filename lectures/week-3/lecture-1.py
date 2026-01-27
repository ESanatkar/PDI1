from xml.etree.ElementTree import tostring
import random
from math import prod
import time

'''
# Exercise 1


  Light Switch
'''

class LightSwitch:
    def __init__(self, state: bool = False, name: str = "") -> None:
        self.state = state
        self.name = "Bedroom"

    def __repr__(self) -> str:
        return f'{self.name!r} {self.__class__.__name__}(state={self.state})'
        
    def __str__(self) -> str:
        return self.name + f' Light is {"on" if self.state else "off"}'

    def turn_on(self) -> None:
        """Turn the switch on."""
        self.state = True
        print(self.name + " light turned on.")

    def turn_off(self) -> None:
        """Turn the switch off."""
        self.state = False
        print(self.name + " light turned off.")
        
light = LightSwitch()
light.turn_on()
print(light.__repr__())
print(light.__str__())

print(light.state)

'''
# Exercise 2


  Dice
'''

class Dice:
    def __init__(self, sides: int = 6, last_roll: None = None) -> None:
        self.sides: int = sides
        self.last_roll = None
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(sides={self.sides})'

    def __str__(self) -> str:
        return "Last roll is " + str(self.last_roll) if self.last_roll else "Not rolled yet."

    def roll(self) -> None:
        """Rolls a number between 1, and sides."""
        self.last_roll = random.randint(1, self.sides)

die = Dice()
print(die.__str__())
die.roll()
print(die.__str__())
print(die.__repr__())