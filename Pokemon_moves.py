"""
포켓몬 기술에 관힌 파일입니다. 하나의 포켓몬은 최대 4개의 기술을 가질 수 있으며 중복될 수 없습니다.
기술은 공격기와 보조기로 구별되며 공격기는 기술의 위력, 명중률, 타입, 부가효가, PP, 우선도, 물리/특수가 들어있으며,
보조기는 기술의 명중률(없는것도 있습니다), 타입, 부가효과, 우선도가 들어있습니다.
"""
import Pokemon_moves_data


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


if __name__ == "__main__":
    absorb = Pokemon_moves_data.movesDict["Absorb"]
    print(absorb)
    move = PokemonAttackMoves(absorb["Type"], absorb["PP"], absorb["Priority"], absorb["Power"], absorb["Accuracy"], absorb["Effect"])

    print(move.effect)