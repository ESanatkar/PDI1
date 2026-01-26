"""
Exercise 5: Dictionaries
TASK: Write both the function and tests

Create a function called personality_mapping that:
- Takes a dictionary mapping villager names to personality types: {"Maple": "Normal", "Raymond": "Smug", "Sherb": "Lazy"}
- Returns a dictionary mapping personality types to lists of villager names: {"Normal": ["Maple"], "Smug": ["Raymond"], "Lazy": ["Sherb"]}
"""


def personality_mapping(villagers: dict[str, str]) -> dict[str, list[str]]:
    """
    Invert a villager-to-personality mapping to a personality-to-villagers mapping.

    Args:
        villagers: Dictionary mapping villager name to personality type

    Returns:
        Dictionary mapping personality type to sorted list of villager names
    """
    
    compiled = {}

    for name, personality in villagers.items():
        if personality not in compiled:
            compiled[personality] = []
        
        compiled[personality].append(name)

    for personality in compiled:
        compiled[personality].sort()

    return compiled

    
# YOUR TESTS HERE (BONUS)
# Write at least 3 tests for invert_personality_mapping
# Test function names must start with "test_"
