"""
포켓몬 기술에 관힌 파일입니다. 하나의 포켓몬은 최대 4개의 기술을 가질 수 있으며 중복될 수 없습니다.
기술은 공격기와 보조기로 구별되며 공격기는 기술의 위력, 명중률, 타입, 부가효가, PP, 우선도, 물리/특수가 들어있으며,
보조기는 기술의 명중률(없는것도 있습니다), 타입, 부가효과, 우선도가 들어있습니다.
"""
import Pokemon_moves_data
from enum import Enum, unique


class PokemonMoves:

    def __init__(self, move_type, pp, priority):
        self._move_type = move_type
        self._pp = pp
        self._priority = priority

    @property
    def move_type(self):
        return self._move_type

    @property
    def pp(self):
        return self._pp

    @property
    def priority(self):
        return self._priority

    # 기술에서 변동될 수 있는 사항은 pp와 우선도뿐이다. pp 원래수치에 따라 변동될수 있는 최대치가 다르다. 이는 추후에 구현
    @pp.setter
    def pp(self, pp):
        self._pp = pp

    @priority.setter
    def priority(self, priority):
        self._priority = priority


class PokemonAttackMoves(PokemonMoves):
    """
    공격기 class 입니다. PokemonMoves 를 상속받았습니다.
    모든 기술이 위력이 있습니다. 명중률은 대부분의 기술들이 있으나 간혹 없는 경우 이는 필중기라는 뜻입니다.
    부가효과가 있는 기술들이 존재합니다.
    """
    def __init__(self, move_type, pp, priority, power, accuracy, effect):
        super().__init__(move_type, pp, priority)
        self._power = power
        self._accuracy = accuracy
        self._effect = effect

    @property
    def power(self):
        return self._power

    @property
    def accuracy(self):
        return self._accuracy

    @property
    def effect(self):
        return self._effect

    # 기술의 원래 위력, 명중률, 부가효과는 보존됩니다. 배틀도중에 변동되는 경우 그때그때 변동값은 따로 계산하면 됩니다.


class PokemonSupportMoves(PokemonMoves):
    """
    보조기 class 입니다. PokemonMoves 를 상속받고 있습니다.
    명중률이 있을 수도 있고 없을 수도 있다는 것이 특징입니다.
    모든 기술들이 부가효과가 있습니다.
    """
    def __init__(self, move_type, pp, priority, accuracy, effect):
        super().__init__(move_type, pp, priority)
        self._accuracy = accuracy
        self._effect = effect

    @property
    def accuracy(self):
        return self._accuracy

    @property
    def effect(self):
        return self._effect


@unique
class PokemonMoveEffectCategory(Enum):
    MOVES_THAT_DO_DAMAGE = 0  # 공격기
    BINDING_MOVES = 1  # 김밥말이, 모래지옥 등
    CONSECUTIVELY_EXECUTED_MOVES = 2
    COUNTERATTACKS = 3
    DECREASED_PRIORITY_MOVES = 4
    EFFECTS_THAT_CAN_MODIFY_MOVE_TYPES = 5
    ENTRY_HAZARD_CREATING_MOVES = 6
    ENTRY_HAZARD_REMOVING_MOVES = 7
    EVOLUTION_INDUCING_MOVES = 8
    FORM_CHANGING_MOVES = 9
    HP_DRAINING_MOVES = 10
    INCREASED_PRIORITY_MOVES = 11
    ITEM_MANIPULATING_MOVES = 12
    MOVE_DRAWING_MOVES = 13
    MOVES_AFFECTED_BY_WEIGHT = 14
    MOVES_BY_STAT_MODIFICATION = 15
    MOVES_BY_USAGE_METHOD = 16
    MOVES_THAT_ACTIVATE_GULP_MISSILE = 17
    MOVES_THAT_AFFECT_ABILITIES = 18
    MOVES_THAT_BECOME_STONGER_AGAINST_A_MINIMIZED_TARGET = 19
    MOVES_THAT_BREAK_THROUGH_PROTECTION = 20
    MOVES_THAT_CALL_OTHER_MOVES = 21
    MOVES_THAT_CAN_CAUSE_CRASH_DAMAGE = 22
    MOVES_THAT_CAN_CAUSE_FLINCHING = 23
    MOVE_THAT_CAN_CHANGE_DAMAGE_CATEGORIES = 24
    MOVES_THAT_CAN_CONFUSE = 25
    MOVES_THAT_CAN_FAIL = 26
    MOVES_THAT_CAN_HEAL_NON_VOLATILE_STATUS_CONDITIONS = 27
    MOVES_THAT_CAN_HIT_SEMI_INVULNERABLE_POKEMONS = 28
    MOVES_THAT_CAN_INFLICT_A_BURN = 29
    MOVES_THAT_CAN_INFLICT_FREEZE = 30
    MOVES_THAT_CAN_INFLICT_PARALYSIS = 31
    MOVES_THAT_CAN_INFLICT_POISON = 32
    MOVES_THAT_CAN_INFLICT_SLEEP = 33
    MOVES_THAT_CAN_JAM = 34
    MOVES_THAT_CANNOT_MISS = 35
    MOVES_THAT_CAUSE_THE_USER_TO_FAINT = 36
    MOVES_THAT_CHANGE_A_POKEMON_TYPE = 37
    MOVES_THAT_CHANGE_TERRAIN = 38
    MOVES_THAT_CHANGE_TYPE = 39
    MOVES_THAT_COST_HP_TO_USE = 40
    MOVES_THAT_DEAL_DIRECT_DAMAGE = 41
    MOVES_THAT_HAVE_RECOIL = 42
    MOVES_THAT_HAVE_SPECIAL_TYPE_EFFECTIVENESS_PROPERTIES = 43
    MOVES_THAT_HAVE_VARIABLE_POWER = 44
    MOVES_THAT_IGNORE_ABILITIES = 45
    MOVES_THAT_POWER_UP = 46
    MOVES_THAT_REMOVE_SOME_TYPE_IMMUNITIES = 47
    MOVES_THAT_REQUIRE_RECHARGING = 48
    MOVES_THAT_RESTORE_HP = 49
    MOVES_THAT_SWITCH_THE_TARGET_OUT = 50
    MOVES_THAT_SWITCH_THE_USER_OUT = 51
    MOVES_THAT_THAW_OUT_THE_USER = 52
    MOVES_THAT_USE_STATS_FROM_DIFFERENT_CATEGORIES = 53
    MOVES_THAT_VARY_WITH_ENVIRONMENT = 54
    MOVES_USABLE_OUTSIDE_OF_BATTLE = 55
    MOVES_WITH_A_CHARGING_TURN = 56
    MOVES_WITH_A_HIGH_CRITICAL_RATIO = 57
    MOVES_WITH_A_PERFECT_CRITICAL_CHANCE = 58
    MOVES_WITH_A_SEMI_INVULNERABLE_TURN = 59
    MOVES_WITH_NO_EFFECT = 60
    MULTI_STRIKE_MOVES = 61
    ONE_HIT_KO_MOVES = 62
    PROTECTION_MOVES = 63
    SCREEN_CREATING_MOVES = 64
    SCREEN_REMOVING_MOVES = 65
    SET_DAMAGE_MOVES = 66
    STATUS_MOVES_THAT_HEAL_THE_USER_IMMEDIATELY = 67
    TRAPPING_MOVES = 68
    WEATHER_CHANGING_MOVES = 69



if __name__ == "__main__":
    absorb = Pokemon_moves_data.movesDict["Absorb"]
    print(absorb)
    move = PokemonAttackMoves(absorb["Type"], absorb["PP"], absorb["Priority"], absorb["Power"], absorb["Accuracy"], absorb["Effect"])

    print(move.effect)
