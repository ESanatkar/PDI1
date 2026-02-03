from trainer import Trainer
from pokemon import Pokemon, FireType, WaterType


def test_team_starts_empty():
    """Test that a new trainer starts with an empty team."""
    trainer = Trainer("Ash")
    assert trainer.get_team_size() == 0
    assert len(trainer.team) == 0


def test_add_to_team_adds_pokemon_successfully():
    """Test that add_to_team successfully adds a Pokemon to the team."""
    trainer = Trainer("Ash")
    pikachu = Pokemon("Pikachu", 35, 10, 8, "Thunder Shock", 40)
    
    result = trainer.add_to_team(pikachu)
    
    assert result == True
    assert trainer.get_team_size() == 1
    assert pikachu in trainer.team


def test_add_to_team_returns_false_when_team_is_full():
    """Test that add_to_team returns False when team is full (6 Pokemon)."""
    trainer = Trainer("Ash")

    for i in range(6):
        pokemon = Pokemon(f"Pidgey", 50, 10, 8, "Tackle", 40)
        result = trainer.add_to_team(pokemon)
        assert result == True
    
    assert trainer.get_team_size() == 6

    extra_pokemon = Pokemon("Flecthling", 50, 10, 8, "Tackle", 40)
    result = trainer.add_to_team(extra_pokemon)
    
    assert result == False
    assert trainer.get_team_size() == 6
    assert extra_pokemon not in trainer.team


def test_get_team_size_returns_correct_count():
    """Test that get_team_size returns the correct number of Pokemon."""
    trainer = Trainer("Ash")
    
    assert trainer.get_team_size() == 0
    
    trainer.add_to_team(Pokemon("Pikachu", 35, 10, 8, "Thunder Shock", 40))
    assert trainer.get_team_size() == 1

    trainer.add_to_team(Pokemon("Charmander", 39, 12, 8, "Ember", 40))
    trainer.add_to_team(Pokemon("Squirtle", 44, 9, 10, "Water Gun", 40))
    assert trainer.get_team_size() == 3


def test_get_first_available_returns_first_non_fainted_pokemon():
    """Test that get_first_available returns the first non-fainted Pokemon."""
    trainer = Trainer("Ash")
    
    pikachu = Pokemon("Pikachu", 35, 10, 8, "Thunder Shock", 40)
    charmander = Pokemon("Charmander", 39, 12, 8, "Ember", 40)
    squirtle = Pokemon("Squirtle", 44, 9, 10, "Water Gun", 40)
    
    trainer.add_to_team(pikachu)
    trainer.add_to_team(charmander)
    trainer.add_to_team(squirtle)
    
    result = trainer.get_first_available()
    
    assert result is pikachu


def test_get_first_available_skips_fainted_pokemon():
    """Test that get_first_available skips fainted Pokemon."""
    trainer = Trainer("Ash")
    
    pikachu = Pokemon("Pikachu", 35, 10, 8, "Thunder Shock", 40)
    charmander = Pokemon("Charmander", 39, 12, 8, "Ember", 40)
    squirtle = Pokemon("Squirtle", 44, 9, 10, "Water Gun", 40)
    bulbasaur = Pokemon("Bulbasaur", 45, 11, 9, "Vine Whip", 45)

    pikachu.current_hp = 0
    charmander.current_hp = 0
    
    trainer.add_to_team(pikachu)
    trainer.add_to_team(charmander)
    trainer.add_to_team(squirtle)
    trainer.add_to_team(bulbasaur)
    
    result = trainer.get_first_available()
    
    assert result is squirtle
    assert result is not pikachu
    assert result is not charmander


def test_get_first_available_returns_none_when_all_fainted():
    """Test that get_first_available returns None when all Pokemon are fainted."""
    trainer = Trainer("Ash")
    
    pikachu = Pokemon("Pikachu", 35, 10, 8, "Thunder Shock", 40)
    charmander = Pokemon("Charmander", 39, 12, 8, "Ember", 40)
    squirtle = Pokemon("Squirtle", 44, 9, 10, "Water Gun", 40)
    
    pikachu.current_hp = 0
    charmander.current_hp = 0
    squirtle.current_hp = 0
    
    trainer.add_to_team(pikachu)
    trainer.add_to_team(charmander)
    trainer.add_to_team(squirtle)
    
    result = trainer.get_first_available()
    
    assert result is None


def test_str_returns_correct_format():
    """Test that __str__ returns the correct format."""
    # Test with empty team
    trainer = Trainer("Ash")
    assert str(trainer) == "Trainer Ash has 0 Pokemon."