from enum import Enum, unique


@unique
class PokemonGender(Enum):
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2