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

def search_pokemon(name):
    """
    데이터베이스에 저장되어 있는 포켓몬을 찾는 함수입니다. 현재 8세대까지 나와있는 포켓몬이
    1,000종이 넘기 때문에 아무래도 눈으로 직접 찾는 것은 어렵기에 이 함수를 만들었습니다.
    :param name: 찾고자하는 포켓몬의 이름.
    :return: Pokemon 클래스에 넣어서 반환합니다.
    """
    pokemon_data = pokemon_dict[name]
    english_name = pokemon_data["English"]
    korean_name = pokemon_data["Korean"]

    if (name == english_name) | (name == korean_name):
        pokemon = Pokemon(pokemon_data["English"], pokemon_data["pokedex"], 50,
                          pokemon_data["type1"], pokemon_data["type2"],pokemon_data["ability1"],
                          "male", PokemonNature.CALM, pokemon_data["egg_group1"],
                          pokemon_data["height"], pokemon_data["weight"], 0, None,
                          pokemon_data["base_hp"],
                          pokemon_data["base_attack"],
                          pokemon_data["base_defense"],
                          pokemon_data["base_sp_attack"],
                          pokemon_data["base_sp_defense"],
                          pokemon_data["base_speed"],
                          0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0,
                          None, None, None, None,
                          True, 0, 0, 0, 0, 0, 0, 0, 0,
                          False, None, False)
    else:
        return -1

    return pokemon


# 어떻게 포켓몬 정보를 클래스에 넣을지 테스트 중입니다.
if __name__ == "__main__":
    bulbasaur = search_pokemon("Bulbasaur")

    print(bulbasaur.name)
