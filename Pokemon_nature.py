"""
포켓몬 성격과 관련된 파일입니다. 포켓몬은 성격에 따라 보너스 스텟을 부여받습니다.
강화되는 스텟은 1.1배, 약화되는 스텟은 0.9배가 됩니다. 총 36가지의 성격이 있고
이 중 6개의 성격은 스텟에 변동이 없는 성격들입니다.
"""
from enum import Enum, unique


@unique
class PokemonNature(Enum):
    # 공격력 1.1배
    LONELY = 1  # 외로움
    ADAMANT = 2  # 고집
    NAUGHTY = 3  # 개구쟁이
    BRAVE = 4  # 용감
    # 방어 1.1배
    BOLD = 5  # 대담
    IMPISH = 6  # 장난꾸러기
    LAX = 7  # 촐랑
    RELAXED = 8  # 무사태평
    # 특공 1.1배
    MODEST = 9  # 조심
    MILD = 10  # 의젓
    RASH = 11  # 덜렁
    QUIET = 12  # 냉정
    # 특방 1.1배
    CALM = 13  # 차분
    GENTLE = 14  # 얌전
    CAREFUL = 15  # 신중
    SASSY = 16  # 건방
    # 스피드 1.1배
    TIMID = 17  # 겁쟁이
    HASTY = 18  # 성급
    JOLLY = 19  # 명랑
    NAIVE = 20  # 천진난만
    # 무보정
    BASHFUL = 21  # 수줍음
    HARDY = 22  # 노력
    DOCILE = 23  # 온순
    QUIRKY = 24  # 변덕
    SERIOUS = 25  # 성실
    
# 각 성격이 어느 스텟은 보정해주는지 반환하는 함수
def determine_nature_bonus(nature):
    """
    boost_stat: 1.1배를 받는 스텟.
    reduce_stat = 0.9배를 받는 스텟
    0: 없음
    1: 공격
    2. 방어
    3. 특공
    4. 특방
    5. 스피드
    :param nature: 성격, PokemonNature 클래스만 받도록 함.
    :return: 어느 스텟이 보정받는지를 반환
    """
    boost_stat = 0
    reduce_stat = 0
    if nature in [PokemonNature.LONELY, PokemonNature.ADAMANT, PokemonNature.NAUGHTY, PokemonNature.BRAVE]:
        boost_stat = 1
        if nature == PokemonNature.LONELY:
            reduce_stat = 2
        elif nature == PokemonNature.ADAMANT:
            reduce_stat = 3
        elif nature == PokemonNature.NAUGHTY:
            reduce_stat = 4
        elif nature == PokemonNature.BRAVE:
            reduce_stat = 5
    elif nature in [PokemonNature.BOLD, PokemonNature.IMPISH, PokemonNature.LAX, PokemonNature.RELAXED]:
        boost_stat = 2
        if nature == PokemonNature.BOLD:
            reduce_stat = 1
        elif nature == PokemonNature.IMPISH:
            reduce_stat = 3
        elif nature == PokemonNature.LAX:
            reduce_stat = 4
        elif nature == PokemonNature.RELAXED:
            reduce_stat = 5
    elif nature in [PokemonNature.MODEST, PokemonNature.MILD, PokemonNature.RASH, PokemonNature.QUIET]:
        boost_stat = 3
        if nature == PokemonNature.MODEST:
            reduce_stat = 1
        elif nature == PokemonNature.MILD:
            reduce_stat = 2
        elif nature == PokemonNature.RASH:
            reduce_stat = 4
        elif nature == PokemonNature.QUIET:
            reduce_stat = 5
    elif nature in [PokemonNature.CALM, PokemonNature.GENTLE, PokemonNature.CAREFUL, PokemonNature.SASSY]:
        boost_stat = 4
        if nature == PokemonNature.CALM:
            reduce_stat = 1
        elif nature == PokemonNature.GENTLE:
            reduce_stat = 2
        elif nature == PokemonNature.CAREFUL:
            reduce_stat = 3
        elif nature == PokemonNature.SASSY:
            reduce_stat = 5
    elif nature in [PokemonNature.TIMID, PokemonNature.HASTY, PokemonNature.JOLLY, PokemonNature.NAIVE]:
        boost_stat = 5
        if nature == PokemonNature.TIMID:
            reduce_stat = 1
        elif nature == PokemonNature.HASTY:
            reduce_stat = 2
        elif nature == PokemonNature.JOLLY:
            reduce_stat = 3
        elif nature == PokemonNature.NAIVE:
            reduce_stat = 4
    else:
        return boost_stat, reduce_stat

    return boost_stat, reduce_stat
