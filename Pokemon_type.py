"""
포켓몬 타입에 관한 파일입니다. 포켓몬에는 총 18가지 타입이 있고
각 타입마다 약점과 반감, 그리고 때로는 무효 상성이 있습니가.
하나의 포켓몬은 최대 두개의 타입을 지니고 있습니다. 포켓몬 기술은
일반적으로 한가지 타입을 가지고 있습니다. 대부분의 경우 상성에 따라
기술의 위력이 변동됩니다. 그러나 간혹 두꺼운지방과 같은 특성이나
프리즈드라이와 같은 일반적인 상성관계에 예외가 되는 경우가 있기 때문에
이를 생각해서 코드를 짭니다. 예외적인 것들은 추후에 추가할 것입니다.
또한 몇몇 타입들은 자체적으로 해당 포켓몬에게 부가효과를 부여합니다.
"""
from enum import Enum, unique


@unique
class PokemonType(Enum):
    NORMAL = 1  # 노말
    FIRE = 2  # 불꽃
    WATER = 3  # 물
    GRASS = 4  # 풀
    ELECTRIC = 5  # 전기
    ICE = 6  # 얼음
    FIGHTING = 7  # 격투
    POISON = 8  # 독
    GROUND = 9  # 땅
    FLYING = 10  # 비행
    PSYCHIC = 11  # 에스퍼
    BUG = 12  # 벌레
    ROCK = 13  # 바위
    GHOST = 14  # 고스트
    DRAGON = 15  # 드래곤
    DARK = 16  # 악
    STEEL = 17  # 강철
    FAIRY = 18  # 페어리


def determine_strength_and_weakness(attacking_type, defending_type):
    """
    상성관계를 따지는 함수입니다. 효과가 굉장하면 2, 보통이면 1, 별로이면 0.5, 없으면 0입니다.
    방어하는 각 타입마다 이 함수를 처리해서 곱연산으로 처리할 예정입니다.
    :param attacking_type: 공격하는 타입. 몇가지 예외를 제외하면 공격기술의 타입은 한가지입니다.
    :param defending_type: 방어하는 포켓몬의 타입으로 1개에서 2개의 타입을 가질 수 있습니다.
                           2개의 타입을 가질 경우, 각각의 상성관계를 따져 곱연산으로 처리합니다.
    :return: 2, 1, 0.5, 0
    """
    # 노말 타입 방어 상성
    if defending_type == PokemonType.NORMAL:
        if attacking_type == PokemonType.FIGHTING:
            return 2
        elif attacking_type == PokemonType.GHOST:
            return 0
        else:
            return 1
    # 불꽃타입 방어 상성
    elif defending_type == PokemonType.FIRE:
        if attacking_type in [PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK]:
            return 2
        elif attacking_type in [PokemonType.FIRE, PokemonType.GRASS, PokemonType.ICE,
                                PokemonType.BUG, PokemonType.STEEL, PokemonType.FAIRY]:
            return 0.5
        else:
            return 1
    # 물타입 방어 상성
    elif defending_type == PokemonType.WATER:
        if attacking_type in [PokemonType.GRASS, PokemonType.ELECTRIC]:
            return 2
        elif attacking_type in [PokemonType.FIRE, PokemonType.WATER, PokemonType.ICE, PokemonType.STEEL]:
            return 0.5
        else:
            return 1
    # 풀타입 방어 상성
    elif defending_type == PokemonType.GRASS:
        if attacking_type in [PokemonType.FIRE, PokemonType.ICE, PokemonType.POISON,
                              PokemonType.FLYING, PokemonType.BUG]:
            return 2
        elif attacking_type in [PokemonType.WATER, PokemonType.GRASS, PokemonType.ELECTRIC, PokemonType.GROUND]:
            return 0.5
        else:
            return 1
    # 전기타입 방어 상성
    elif defending_type == PokemonType.ELECTRIC:
        if attacking_type == PokemonType.GROUND:
            return 2
        elif attacking_type in [PokemonType.ELECTRIC, PokemonType.FLYING, PokemonType.STEEL]:
            return 0.5
        else:
            return 1
    # 얼음타입 방어 상성
    elif defending_type == PokemonType.ICE:
        if attacking_type in [PokemonType.FIRE, PokemonType.FIGHTING, PokemonType.ROCK, PokemonType.STEEL]:
            return 2
        elif attacking_type == PokemonType.ICE:
            return 0.5
        else:
            return 1
    # 격투타입 방어 상성
    elif defending_type == PokemonType.FIGHTING:
        if attacking_type in [PokemonType.FLYING, PokemonType.PSYCHIC, PokemonType.FAIRY]:
            return 2
        elif attacking_type in [PokemonType.BUG, PokemonType.ROCK, PokemonType.DARK]:
            return 0.5
        else:
            return 1
    # 독타입 방어 상성
    elif defending_type == PokemonType.POISON:
        if attacking_type in [PokemonType.GROUND, PokemonType.PSYCHIC]:
            return 2
        elif attacking_type in [PokemonType.GRASS, PokemonType.FIGHTING, PokemonType.POISON,
                                PokemonType.BUG, PokemonType.FAIRY]:
            return 0.5
        else:
            return 1
    # 땅타입 방어 상성
    elif defending_type == PokemonType.GROUND:
        if attacking_type in [PokemonType.WATER, PokemonType.GRASS, PokemonType.ICE]:
            return 2
        elif attacking_type in [PokemonType.POISON, PokemonType.ROCK]:
            return 0.5
        elif attacking_type == PokemonType.ELECTRIC:
            return 0
        else:
            return 1
    # 비행타입 방어 상성
    elif defending_type == PokemonType.FLYING:
        if attacking_type in [PokemonType.ELECTRIC, PokemonType.ICE, PokemonType.ROCK]:
            return 2
        elif attacking_type in [PokemonType.GRASS, PokemonType.FIGHTING, PokemonType.BUG]:
            return 0.5
        elif attacking_type == PokemonType.GROUND:
            return 0
        else:
            return 1
    # 에스퍼 방어 상성
    if defending_type == PokemonType.PSYCHIC:
        if attacking_type in [PokemonType.BUG, PokemonType.GHOST, PokemonType.DARK]:
            return 2
        elif attacking_type in [PokemonType.FIGHTING, PokemonType.PSYCHIC]:
            return 0.5
        else:
            return 1
    # 벌레타입 방어 상성
    if defending_type == PokemonType.BUG:
        if attacking_type in [PokemonType.FIRE, PokemonType.FLYING, PokemonType.ROCK]:
            return 2
        elif attacking_type in [PokemonType.GRASS, PokemonType.FIGHTING, PokemonType.GROUND]:
            return 0.5
        else:
            return 1
    # 바위타입 방어 상성
    if defending_type == PokemonType.ROCK:
        if attacking_type in [PokemonType.WATER, PokemonType.GRASS, PokemonType.FIGHTING,
                              PokemonType.GROUND, PokemonType.STEEL]:
            return 2
        elif attacking_type in [PokemonType.NORMAL, PokemonType.FIRE, PokemonType.POISON, PokemonType.FLYING]:
            return 0.5
        else:
            return 1
    # 고스트타입 방어 상성
    if defending_type == PokemonType.GHOST:
        if attacking_type in [PokemonType.GHOST, PokemonType.DARK]:
            return 2
        elif attacking_type in [PokemonType.POISON, PokemonType.BUG]:
            return 0.5
        elif attacking_type in [PokemonType.NORMAL, PokemonType.FIGHTING]:
            return 0
        else:
            return 1
    # 드래곤타입 방어 상성
    if defending_type == PokemonType.DRAGON:
        if attacking_type in [PokemonType.ICE, PokemonType.DRAGON, PokemonType.FAIRY]:
            return 2
        elif attacking_type in [PokemonType.FIRE, PokemonType.WATER, PokemonType.GRASS, PokemonType.ELECTRIC]:
            return 0.5
        else:
            return 1
    # 악타입 방어 상성
    if defending_type == PokemonType.DARK:
        if attacking_type in [PokemonType.FIGHTING, PokemonType.BUG, PokemonType.FAIRY]:
            return 2
        elif attacking_type in [PokemonType.GHOST, PokemonType.DARK]:
            return 0.5
        elif attacking_type == PokemonType.PSYCHIC:
            return 0
        else:
            return 1
    # 강철타입 방어 상성
    if defending_type == PokemonType.STEEL:
        if attacking_type in [PokemonType.FIRE, PokemonType.FIGHTING, PokemonType.GROUND]:
            return 2
        elif attacking_type in [PokemonType.NORMAL, PokemonType.GRASS, PokemonType.ICE,
                                PokemonType.FLYING, PokemonType.PSYCHIC, PokemonType.BUG,
                                PokemonType.ROCK, PokemonType.DRAGON, PokemonType.STEEL, PokemonType.FAIRY]:
            return 0.5
        elif attacking_type == PokemonType.POISON:
            return 0
        else:
            return 1
    # 페어리타입 방어 상성
    if defending_type == PokemonType.FAIRY:
        if attacking_type in [PokemonType.POISON, PokemonType.STEEL]:
            return 2
        elif attacking_type in [PokemonType.FIGHTING, PokemonType.BUG, PokemonType.DARK]:
            return 0.5
        elif attacking_type == PokemonType.DRAGON:
            return 0
        else:
            return 1


if __name__ == "__main__":
    print(determine_strength_and_weakness(PokemonType.ELECTRIC, PokemonType.GROUND))