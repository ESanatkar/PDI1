from pokemon import Pokemon, FireType, WaterType

def test_health_is_equal():
    current_pokemon =  Pokemon("Eevee", 55, 10, 8, "Tackle", 40)
    assert current_pokemon.max_hp == current_pokemon.current_hp

def test_is_fainted():
    current_pokemon =  Pokemon("Eevee", 55, 10, 8, "Tackle", 40)
    assert not current_pokemon.is_fainted()

    current_pokemon.current_hp = 0
    assert current_pokemon.is_fainted()

def test_proper_move_description():
    current_pokemon =  Pokemon("Eevee", 55, 10, 8, "Tackle", 40)
    assert current_pokemon.attack_move() == "Eevee uses Tackle!"

def test_description():
    current_pokemon =  Pokemon("Eevee", 55, 10, 8, "Tackle", 40)
    assert current_pokemon.__str__() == f"Eevee (HP: {current_pokemon.current_hp}/{current_pokemon.max_hp})"

def test_fire_type_description():
    charmander = FireType("Charmander", 39, 11, 5, "Ember", 35, 0.1)
    assert charmander.description() == "Charmander is a Fire type Pokemon with 10.0% burn chance."

def test_water_type_description():
    squirtle = WaterType("Squirtle", 44, 9, 7, "Water Gun", 40, 25)
    assert squirtle.description() == "Squirtle is a Water type Pokemon with swim speed 25."

def test_normal_type_description():
    eevee =  Pokemon("Eevee", 55, 10, 8, "Tackle", 40)
    assert eevee.__str__() == "Eevee (HP: 55/55)"