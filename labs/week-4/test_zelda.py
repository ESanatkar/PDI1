#!/usr/bin/env python3

import pytest
from zelda import Item, Weapon, Enemy, Inventory, Room, Dungeon


'''
# Exercise 1.1

    Indexing
'''


def test_inventory_getitem_first():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    assert inventory[0].name == "Rupee"


def test_inventory_getitem_negative_index():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    assert inventory[-1].name == "Bomb"
    assert inventory[-2].name == "Rupee"


def test_inventory_getitem_slicing():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    inventory.add_item(Item("Heart", value=100))
    
    sliced: Item | list[Item] = inventory[0:2]
    assert len(sliced) == 2
    assert sliced[0].name == "Rupee"
    assert sliced[1].name == "Bomb"


def test_inventory_getitem_empty_index_error():
    inventory = Inventory()
    with pytest.raises(IndexError):
        _ = inventory[0]


def test_inventory_getitem_invalid_index_error():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    with pytest.raises(IndexError):
        _ = inventory[5]


'''
# Exercise 1.2

    Modification
'''

def test_inventory_setitem_replace():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    
    new_item = Item("Heart", value=100)
    inventory[0] = new_item
    
    assert inventory[0].name == "Heart"
    assert inventory[0].value == 100


def test_inventory_setitem_negative_index():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    
    new_item = Item("Arrow", value=5)
    inventory[-1] = new_item
    
    assert inventory[-1].name == "Arrow"


def test_inventory_setitem_invalid_index_raises_index_error():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    
    with pytest.raises(IndexError):
        inventory[10] = Item("Bomb", value=20)


'''
# Exercise 1.3

    Length Checks
'''

def test_inventory_len_empty():
    inventory = Inventory()
    assert len(inventory) == 0


def test_inventory_len_with_items():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    inventory.add_item(Item("Heart", value=100))
    assert len(inventory) == 3


def test_inventory_len_updates_after_adding():
    inventory = Inventory()
    assert len(inventory) == 0
    
    inventory.add_item(Item("Rupee", value=1))
    assert len(inventory) == 1
    
    inventory.add_item(Item("Bomb", value=20))
    assert len(inventory) == 2


def test_inventory_bool_empty_is_falsy():
    inventory = Inventory()
    assert not inventory


def test_inventory_bool_nonempty_is_truthy():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    assert inventory


'''
# Exercise 1.1

    Indexing
'''

def test_inventory_iter_all_items():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    
    names = [item.name for item in inventory]
    assert names == ["Rupee", "Bomb"]


def test_inventory_iter_empty():
    inventory = Inventory()
    items = list(inventory)
    assert items == []


def test_inventory_iter_order():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    inventory.add_item(Item("Heart", value=100))
    
    names = [item.name for item in inventory]
    assert names == ["Rupee", "Bomb", "Heart"]


def test_inventory_iter_list_conversion():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    
    items_list = list(inventory)
    assert len(items_list) == 2
    assert items_list[0].name == "Rupee"


'''
# Exercise 1.5

    Item Iteration
'''

def test_inventory_iter_valuable_filters_correctly():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Heart", value=100))
    inventory.add_item(Item("Bomb", value=20))
    
    valuable = list(inventory.iter_valuable(50))
    assert len(valuable) == 1
    assert valuable[0].name == "Heart"


def test_inventory_iter_valuable_none_match():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    
    valuable = list(inventory.iter_valuable(100))
    assert len(valuable) == 0


def test_inventory_iter_valuable_all_match():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Heart", value=100))
    inventory.add_item(Item("Bomb", value=20))
    
    valuable = list(inventory.iter_valuable(0))
    assert len(valuable) == 3


def test_inventory_iter_valuable_exact_threshold():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    inventory.add_item(Item("Heart", value=100))
    
    valuable = list(inventory.iter_valuable(20))
    assert len(valuable) == 2
    assert valuable[0].name == "Bomb"
    assert valuable[1].name == "Heart"


'''
# Exercise 1.6

    Existence Checks
'''

def test_inventory_contains_by_name_found():
    inventory = Inventory()
    inventory.add_item(Item("Bomb", value=20))
    assert "Bomb" in inventory


def test_inventory_contains_by_name_not_found():
    inventory = Inventory()
    inventory.add_item(Item("Bomb", value=20))
    assert "Rupee" not in inventory


def test_inventory_contains_empty():
    inventory = Inventory()
    assert "Bomb" not in inventory


def test_inventory_contains_by_object():
    inventory = Inventory()
    rupee = Item("Rupee", value=1)
    inventory.add_item(rupee)
    
    same_rupee = Item("Rupee", value=50)
    assert same_rupee in inventory


'''
# Exercise 2.1

    Boolean Checks
'''

def test_item_eq_same_name():
    item1 = Item("Rupee", value=1)
    item2 = Item("Rupee", value=50)
    assert item1 == item2


def test_item_eq_different_name():
    item1 = Item("Rupee", value=1)
    item2 = Item("Bomb", value=20)
    assert not (item1 == item2)


def test_item_eq_with_string():
    item = Item("Rupee", value=1)
    assert not (item == "Rupee")


def test_item_eq_identity():
    item = Item("Rupee", value=1)
    assert item == item


def test_item_eq_different_value_same_name():
    item1 = Item("Heart", value=100, quantity=1)
    item2 = Item("Heart", value=50, quantity=5)
    assert item1 == item2


'''
# Exercise 2.2

 Order Checks
'''

def test_enemy_eq_same_name():
    enemy1 = Enemy("Bokoblin", health=50, strength=10)
    enemy2 = Enemy("Bokoblin", health=100, strength=20)
    assert enemy1 == enemy2


def test_enemy_eq_different_name():
    enemy1 = Enemy("Bokoblin", health=50, strength=10)
    enemy2 = Enemy("Lynel", health=500, strength=50)
    assert not (enemy1 == enemy2)


def test_enemy_lt_by_strength():
    weak = Enemy("Bokoblin", health=50, strength=10)
    strong = Enemy("Lynel", health=500, strength=50)
    assert weak < strong


def test_enemy_lt_equal_strength():
    enemy1 = Enemy("Bokoblin", health=50, strength=10)
    enemy2 = Enemy("Moblin", health=100, strength=10)
    assert not (enemy1 < enemy2)


def test_enemy_sort_by_strength():
    enemies = [
        Enemy("Lynel", health=500, strength=50),
        Enemy("Bokoblin", health=50, strength=10),
        Enemy("Moblin", health=100, strength=25),
    ]
    enemies.sort()
    names = [e.name for e in enemies]
    assert names == ["Bokoblin", "Moblin", "Lynel"]


def test_enemy_sort_multiple_same_strength():
    enemies = [
        Enemy("Strong", health=100, strength=50),
        Enemy("Weak", health=50, strength=10),
        Enemy("Medium", health=75, strength=25),
        Enemy("AlsoWeak", health=60, strength=10),
    ]
    enemies.sort()
    strengths = [e.strength for e in enemies]
    assert strengths == [10, 10, 25, 50]


'''
# Exercise 2.3

    Item Hashes
'''

def test_item_hash_equal_items_same_hash():
    item1 = Item("Rupee", value=1)
    item2 = Item("Rupee", value=50)
    assert hash(item1) == hash(item2)


def test_item_hash_in_set():
    item1 = Item("Rupee", value=1)
    item2 = Item("Rupee", value=50)
    item3 = Item("Bomb", value=20)
    
    unique_items = {item1, item2, item3}
    assert len(unique_items) == 2


def test_item_hash_as_dict_key():
    item1 = Item("Rupee", value=1)
    item2 = Item("Rupee", value=50)
    item3 = Item("Bomb", value=20)
    
    item_counts = {}
    item_counts[item1] = 5
    item_counts[item2] = 10
    item_counts[item3] = 3
    
    assert len(item_counts) == 2
    assert item_counts[item1] == 10


def test_item_hash_different_names_different_hash():
    item1 = Item("Rupee", value=1)
    item2 = Item("Bomb", value=20)
    assert hash(item1) != hash(item2)


'''
# Exercise 2.4

    Weapon Hashes
'''
def test_weapon_eq_same_name_different_durability():
    sword1 = Weapon("Master Sword", damage=30, durability=100)
    sword2 = Weapon("Master Sword", damage=30, durability=50)
    assert sword1 == sword2


def test_weapon_eq_different_name():
    sword1 = Weapon("Master Sword", damage=30, durability=100)
    sword2 = Weapon("Rusty Sword", damage=5, durability=20)
    assert not (sword1 == sword2)


def test_weapon_eq_same_name_different_damage():
    sword1 = Weapon("Master Sword", damage=30, durability=100)
    sword2 = Weapon("Master Sword", damage=50, durability=100)
    assert sword1 == sword2


def test_weapon_hash_in_set():
    sword1 = Weapon("Master Sword", damage=30, durability=100)
    sword2 = Weapon("Master Sword", damage=30, durability=50)
    rusty = Weapon("Rusty Sword", damage=5, durability=20)
    
    weapons = {sword1, sword2, rusty}
    assert len(weapons) == 2


def test_weapon_hash_as_dict_key():
    sword1 = Weapon("Master Sword", damage=30, durability=100)
    sword2 = Weapon("Master Sword", damage=30, durability=50)
    rusty = Weapon("Rusty Sword", damage=5, durability=20)
    
    weapon_inventory = {}
    weapon_inventory[sword1] = 1
    weapon_inventory[sword2] = 2
    weapon_inventory[rusty] = 5
    
    assert len(weapon_inventory) == 2
    assert weapon_inventory[sword1] == 2


def test_weapon_hash_equal_weapons_same_hash():
    sword1 = Weapon("Master Sword", damage=30, durability=100)
    sword2 = Weapon("Master Sword", damage=50, durability=20)
    assert hash(sword1) == hash(sword2)


'''
# Exercise 3.1

    Room Checks
'''

def test_room_bool_with_enemies_is_truthy():
    room = Room("Eastern Chamber")
    room.add_enemy(Enemy("Bokoblin", 50, 10))
    assert room


def test_room_bool_cleared_is_falsy():
    room = Room("Eastern Chamber")
    room.add_enemy(Enemy("Bokoblin", 50, 10))
    room.cleared = True
    assert not room


def test_room_bool_empty_is_falsy():
    room = Room("Eastern Chamber")
    assert not room


def test_room_bool_cleared_empty_is_falsy():
    room = Room("Eastern Chamber")
    room.cleared = True
    assert not room


def test_room_bool_multiple_enemies_not_cleared():
    room = Room("Boss Chamber")
    room.add_enemy(Enemy("Bokoblin", 50, 10))
    room.add_enemy(Enemy("Moblin", 100, 25))
    assert room


'''
# Exercise 3.2

    Indexing
'''

def test_dungeon_getitem():
    dungeon = Dungeon("Forest Temple")
    dungeon.add_room(Room("Entry Hall"))
    dungeon.add_room(Room("Boss Room"))
    assert dungeon[0].name == "Entry Hall"
    assert dungeon[-1].name == "Boss Room"


def test_dungeon_getitem_negative_index():
    dungeon = Dungeon("Forest Temple")
    dungeon.add_room(Room("Entry Hall"))
    dungeon.add_room(Room("Middle Room"))
    dungeon.add_room(Room("Boss Room"))
    assert dungeon[-1].name == "Boss Room"
    assert dungeon[-2].name == "Middle Room"


def test_dungeon_getitem_invalid_index():
    dungeon = Dungeon("Forest Temple")
    dungeon.add_room(Room("Entry Hall"))
    with pytest.raises(IndexError):
        _ = dungeon[5]


def test_dungeon_len():
    dungeon = Dungeon("Forest Temple")
    assert len(dungeon) == 0
    
    dungeon.add_room(Room("Entry Hall"))
    assert len(dungeon) == 1
    
    dungeon.add_room(Room("Boss Room"))
    assert len(dungeon) == 2


def test_dungeon_len_empty():
    dungeon = Dungeon("Water Temple")
    assert len(dungeon) == 0


def test_dungeon_iter():
    dungeon = Dungeon("Forest Temple")
    dungeon.add_room(Room("Entry Hall"))
    dungeon.add_room(Room("Middle Room"))
    dungeon.add_room(Room("Boss Room"))
    
    room_names = [room.name for room in dungeon]
    assert room_names == ["Entry Hall", "Middle Room", "Boss Room"]


def test_dungeon_iter_empty():
    dungeon = Dungeon("Fire Temple")
    rooms = list(dungeon)
    assert rooms == []


def test_dungeon_contains_by_name():
    dungeon = Dungeon("Forest Temple")
    dungeon.add_room(Room("Boss Room"))
    assert "Boss Room" in dungeon
    assert "Secret Room" not in dungeon


def test_dungeon_contains_by_object():
    dungeon = Dungeon("Forest Temple")
    boss_room = Room("Boss Room")
    dungeon.add_room(boss_room)
    
    same_room = Room("Boss Room")
    assert same_room in dungeon


def test_dungeon_contains_empty():
    dungeon = Dungeon("Shadow Temple")
    assert "Boss Room" not in dungeon


def test_dungeon_iter_uncleared():
    dungeon = Dungeon("Forest Temple")
    room1 = Room("Entry Hall")
    room2 = Room("Boss Room")
    room3 = Room("Treasure Room")
    
    room1.cleared = True
    dungeon.add_room(room1)
    dungeon.add_room(room2)
    dungeon.add_room(room3)
    
    uncleared = list(dungeon.iter_uncleared())
    assert len(uncleared) == 2
    assert uncleared[0].name == "Boss Room"
    assert uncleared[1].name == "Treasure Room"


def test_dungeon_iter_uncleared_all_cleared():
    dungeon = Dungeon("Forest Temple")
    room1 = Room("Entry Hall")
    room2 = Room("Boss Room")
    
    room1.cleared = True
    room2.cleared = True
    
    dungeon.add_room(room1)
    dungeon.add_room(room2)
    
    uncleared = list(dungeon.iter_uncleared())
    assert len(uncleared) == 0


def test_dungeon_iter_uncleared_none_cleared():
    dungeon = Dungeon("Forest Temple")
    dungeon.add_room(Room("Entry Hall"))
    dungeon.add_room(Room("Boss Room"))
    dungeon.add_room(Room("Treasure Room"))
    
    uncleared = list(dungeon.iter_uncleared())
    assert len(uncleared) == 3