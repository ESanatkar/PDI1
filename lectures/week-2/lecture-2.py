from itertools import count
from math import prod
import time

'''
# Exercise 1


   Sets
'''

student_ids: list[int] = [101, 102, 103, 101, 104, 102, 105, 103]

class_a: set[str] = {'Angus', 'Bubbles', 'Chester', 'Daisy'}
class_b: set[str] = {'Chester', 'Daisy', 'Eve', 'Frita'}

both_classes: set[str] = class_a & class_b
print(both_classes)

either_classes: set[str] = class_a | class_b
print(either_classes)

only_a: set[str] = class_a - class_b
print(only_a)

only_one_class: set[str] = class_a ^ class_b
print(only_one_class)

'''
# Exercise 2


   Dictionaries
'''

scores: dict[str, int] = {'Angus': 85, 'Bubbles': 92, 'Chester': 78, 'Daisy': 95, 'Eve': 88, 'Jeremiah': 64}

scores_above_75: dict[str, int] = {k: v for k, v in scores.items() if v > 75}
print(scores_above_75)

def count_letters(text: str) -> dict[str, int]:
    """Returns a dictionary with letter counts of a word."""
    counts: dict = {}
    for letter in text.lower():
        print(letter)
        counts[letter] = counts.get(letter, 0) + 1
    return counts

print(count_letters("hello"))

inventory: dict[str, int] = {
    'apples': 50,
    'bananas': 30,
    'oranges': 45,
    'pears': 20
}

inventory["grapes"] = 35
print(inventory)

inventory["apples"] -= 10
print(inventory)

if "Mangoes" in inventory:
    print("There are mangoes in stock.")
else:
    print("There are no mangoes in stock.")

for key,value in inventory.items():
    if value < 25 :
        print(key)

print(inventory)
restocked_inventory: dict[str, float] = {k: v*1.1 for k, v in inventory.items()}
print(restocked_inventory)