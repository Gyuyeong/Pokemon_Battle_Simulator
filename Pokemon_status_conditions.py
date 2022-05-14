"""
상태이상에 관한 파일입니다. 메이저한(지속성) 상태이상(독, 맹독, 마비, 화상, 얼음, 잠듦)은 중첩될 수 없습니다.
헤롱헤롱처럼 상태창에 나타나지 않는 상태이상(일회성 상태이상, 교체, 일정 턴이 지남 또는 배틀에서 벗어나면 풀림)은 중첩될 수 있습니다.
포켓몬이 기절했을 경우, 기절 이외의 어떠한 상태도 중첩될 수 없습니다.
"""
from enum import Enum, unique


@unique
class PokemonStatusConditions(Enum):
    # 지속성 상태변화
    POISON = 1  # 독
    TOXIC = 2  # 맹독
    BURN = 3  # 화상
    PARALYZE = 4  # 마비
    ASLEEP = 5  # 잠듦
    ICE = 6  # 얼음
    # 일회성 상태변화
    CONFUSION = 7  # 혼란
    FLINCH = 8  # 풀죽음
    UNSWITCHABLE = 9  # 교체불가
    ATTRACTED = 10  # 헤롱헤롱
    CANNOT_USE_SKILL = 11  # 기술사용불가
    CANNOT_USE_TOOLS = 12  # 도구사용불가
    PERISH_SONG = 13  # 멸망의노래
    DESTINY_BOND = 14  # 길동무
    CURSE = 15  # 고스트타입의 저주
    POWDER = 16  # 분진(1턴간 상대를 분진상태로 만듦. 분진상태의 포켓몬이 불꽃기술을 사용하면 체력 1/4 데미지 및 그 기술 무효)
    