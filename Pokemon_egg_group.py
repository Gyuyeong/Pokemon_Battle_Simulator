"""
교배그룹을 보아놓은 파일입니다.
"""
from enum import Enum, unique


@unique
class PokemonEggGroup(Enum):
    MONSTER = 1  # 괴수 그룹
    WATER1 = 2  # 수중1그룹
    WATER2 = 3  # 수중2그룹
    WATER3 = 4  # 수중3그룹
    BUG = 5  # 벌레그룹
    FLYING = 6  # 비행그룹
    FIELD = 7  # 육상그룹
    FAIRY = 8  # 요정그룹
    GRASS = 9  # 식물그룹
    HUMANLIKE = 10  # 인간형그룹
    MINERAL = 11  # 광물그룹
    AMORPHOUS = 12  # 부정형그룹
    DITTO = 13  # 메타몽그룹
    DRAGON = 14  # 드래곤그룹
    NOEGGSDISCOVERED = 15  # 알미발견
    GENDERUNKNOWN = 16  # 성별 불명

