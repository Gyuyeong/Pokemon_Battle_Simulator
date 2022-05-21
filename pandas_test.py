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

pokemon1 = dict()
pokemon2 = dict()
pokemon3 = dict()

pokemon1["name"] = "Abomosnow"
pokemon1["pokedex_number"] = 460
pokemon1["korean_name"] = "눈설왕"
pokemon1["type1"] = "Grass"
pokemon1["type2"] = "Ice"

pokemon2["name"] = "Abra"
pokemon2["pokedex_number"] = 63
pokemon2["korean_name"] = "캐이시"
pokemon2["type1"] = "Psychic"
pokemon2["type2"] = "None"

pokemon3["name"] = "Absol"
pokemon3["pokedex_number"] = 359
pokemon3["korean_name"] = "앱솔"
pokemon3["type1"] = "Dark"
pokemon3["type2"] = "None"

df = pd.DataFrame([pokemon1, pokemon2, pokemon3])

print(df.head())