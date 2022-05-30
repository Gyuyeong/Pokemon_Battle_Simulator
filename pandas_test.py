# import pandas as pd
#
# names = ["Abomosnow", "Abra", "Absol"]
# pokedex_numbers = [460, 63, 359]
# korean_name = ["눈설왕", "캐이시", "앱솔"]
# type1 = ["Grass", "Psychic", "Dark"]
# type2 = ["Ice", "None", "None"]
# normal_abilities = ["Snow Warning", "Sychronize or Inner Focus", "Pressure or Super Luck"]
# hidden_abilities = ["Soundproof", "Magic Guard", "Justified"]
# mega_abilities = ["Snow Warning", "None", "Magic Bounce"]
#
# df = pd.DataFrame([names, pokedex_numbers, korean_name, type1, type2, normal_abilities, hidden_abilities, mega_abilities]).transpose()
#
# print(df.head())
import pandas as pd

# pokemon1 = dict()
# pokemon2 = dict()
# pokemon3 = dict()
#
# pokemon1["name"] = "Abomosnow"
# pokemon1["pokedex_number"] = 460
# pokemon1["korean_name"] = "눈설왕"
# pokemon1["type1"] = "Grass"
# pokemon1["type2"] = "Ice"
#
# pokemon2["name"] = "Abra"
# pokemon2["pokedex_number"] = 63
# pokemon2["korean_name"] = "캐이시"
# pokemon2["type1"] = "Psychic"
# pokemon2["type2"] = "None"
#
# pokemon3["name"] = "Absol"
# pokemon3["pokedex_number"] = 359
# pokemon3["korean_name"] = "앱솔"
# pokemon3["type1"] = "Dark"
# pokemon3["type2"] = "None"
#
# df = pd.DataFrame([pokemon1, pokemon2, pokemon3])
#
# print(df.head())

pokemons = list()

name = "Abomasnow"
pokedex_number = 460
pokemon_type = ['Grass', 'Ice']
pokemon_abilities = ['Snow Warning', 'Soundproof', 'Snow Warning']
pokemon_stats = [90, 92, 75, 92, 85, 60]
pokemon_heights = ['7\'03"\n', '2.2 m\n']
pokemon_weights = ['298.7 lbs.\n', '135.5 kg\n']

pokemon1 = dict()
pokemon1["name"] = name
pokemon1["pokedex_number"] = pokedex_number
pokemon1["type1"] = pokemon_type[0]
pokemon1["type2"] = pokemon_type[1]
pokemon1["abilities"] = pokemon_abilities
pokemon1["hp"] = pokemon_stats[0]
pokemon1["atk"] = pokemon_stats[1]
pokemon1["def"] = pokemon_stats[2]
pokemon1["sp_atk"] = pokemon_stats[3]
pokemon1["sp_def"] = pokemon_stats[4]
pokemon1["speed"] = pokemon_stats[5]
pokemon1["height(in)"] = pokemon_heights[0]
pokemon1["height(m)"] = pokemon_heights[1]
pokemon1["weight(lbs)"] = pokemon_weights[0]
pokemon1["weight(kg)"] = pokemon_weights[1]

pokemon2 = dict()
pokemon2["name"] = name
pokemon2["pokedex_number"] = pokedex_number
pokemon2["type1"] = pokemon_type[0]
pokemon2["type2"] = pokemon_type[1]
pokemon2["abilities"] = pokemon_abilities
pokemon2["hp"] = pokemon_stats[0]
pokemon2["atk"] = pokemon_stats[1]
pokemon2["def"] = pokemon_stats[2]
pokemon2["sp_atk"] = pokemon_stats[3]
pokemon2["sp_def"] = pokemon_stats[4]
pokemon2["speed"] = pokemon_stats[5]
pokemon2["height(in)"] = pokemon_heights[0]
pokemon2["height(m)"] = pokemon_heights[1]
pokemon2["weight(lbs)"] = pokemon_weights[0]
pokemon2["weight(kg)"] = pokemon_weights[1]

pokemons.append(pokemon1)
pokemons.append(pokemon2)

df = pd.DataFrame(pokemons)
print(df["abilities"])