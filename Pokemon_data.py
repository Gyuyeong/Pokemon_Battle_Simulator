"""
모든 포켓몬들을 모아놓은 파일입니다.
"""
from Pokemon import Pokemon
from Pokemon_type import PokemonType
from Pokemon_nature import PokemonNature

pokemon_dict = {
    "Bulbasaur": {
        "English": "Bulbasaur",
        "Korean": "이상해씨",
        "pokedex": 1,
        "type1": PokemonType.GRASS,
        "type2": PokemonType.POISON,
        "ability1": "Overgrow",
        "ability2": "Chlorophyll",
        "ability3": None,
        "height": 0.7,
        "weight": 6.9,
        "egg_group1": "Monster",
        "egg_group2": "Grass",
        "base_hp": 45,
        "base_attack": 49,
        "base_defense": 49,
        "base_sp_attack": 65,
        "base_sp_defense": 65,
        "base_speed": 45,
        "can_evolve": True,
        "is_legendary": False
    }
}

# 어떻게 포켓몬 정보를 클래스에 넣을지 테스트 중입니다.
if __name__ == "__main__":
    print(pokemon_dict["Bulbasaur"]["English"])

    bulbasaur = Pokemon(pokemon_dict["Bulbasaur"]["English"], pokemon_dict["Bulbasaur"]["pokedex"], 50,
                        pokemon_dict["Bulbasaur"]["type1"], pokemon_dict["Bulbasaur"]["type2"],
                        pokemon_dict["Bulbasaur"]["ability2"], "male", PokemonNature.CALM,
                        pokemon_dict["Bulbasaur"]["egg_group1"], pokemon_dict["Bulbasaur"]["height"],
                        pokemon_dict["Bulbasaur"]["weight"], 0, None,
                        pokemon_dict["Bulbasaur"]["base_hp"],
                        pokemon_dict["Bulbasaur"]["base_attack"],
                        pokemon_dict["Bulbasaur"]["base_defense"],
                        pokemon_dict["Bulbasaur"]["base_sp_attack"],
                        pokemon_dict["Bulbasaur"]["base_sp_defense"],
                        pokemon_dict["Bulbasaur"]["base_speed"],
                        31, 31, 31, 31, 31, 31,
                        252, 0, 0, 0, 252, 4,
                        None, None, None, None,
                        pokemon_dict["Bulbasaur"]["can_evolve"],
                        0, 0, 0, 0, 0, 0, 0, 0, False, None, False)

    print(bulbasaur.name)
