"""
플레이어에 관한 파일입니다. 한 플레이어는 최대 6마리의 포켓몬을 지닐 수 있습니다. 6마리의 포켓몬은 모두 달라야합니다.
배틀을 하기전 선출을 정하는데, 싱글의 경우 3마리, 더블의 경우 4마리를 원하는 순서로 골라서 배틀에 내보냅니다.
포켓몬이 부족할 경우 배틀에 참여할 수 없습니다.
자신의 엔트리에 있는 포켓몬들간 지닌도구는 중복될 수 없습니다. (ex. 구애안경을 2마리 이상의 포켓몬이 지니는 것 불가)
"""
from Pokemon import Pokemon


class Player:
    def __init__(self, pokemon1=None, pokemon2=None, pokemon3=None,
                 pokemon4=None, pokemon5=None, pokemon6=None):
        self._pokemon1 = pokemon1
        self._pokemon2 = pokemon2
        self._pokemon3 = pokemon3
        self._pokemon4 = pokemon4
        self._pokemon5 = pokemon5
        self._pokemon6 = pokemon6
        self._entry = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]

    @property
    def pokemon1(self):
        return self._pokemon1

    @property
    def pokemon2(self):
        return self._pokemon2

    @property
    def pokemon3(self):
        return self._pokemon3

    @property
    def pokemon4(self):
        return self._pokemon4

    @property
    def pokemon5(self):
        return self._pokemon5

    @property
    def pokemon6(self):
        return self._pokemon6

    @pokemon1.setter
    def pokemon1(self, pokemon=Pokemon):
        self._pokemon1 = pokemon

    @pokemon2.setter
    def pokemon2(self, pokemon=Pokemon):
        self._pokemon2 = pokemon

    @pokemon3.setter
    def pokemon3(self, pokemon=Pokemon):
        self._pokemon3 = pokemon

    @pokemon4.setter
    def pokemon4(self, pokemon=Pokemon):
        self._pokemon4 = pokemon

    @pokemon5.setter
    def pokemon5(self, pokemon=Pokemon):
        self._pokemon5 = pokemon

    @pokemon6.setter
    def pokemon6(self, pokemon=Pokemon):
        self._pokemon1 = pokemon


if __name__ == "__main__":
    player = Player(1)
    print(player._entry)