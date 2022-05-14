"""
포켓몬 배틀에 관한 파일입니다. 배틀을 하나의 클래스로 만들어서 각 배틀을 개체로 만들어봅니다.
포켓몬은 턴제 게임입니다.양쪽이 매턴 자신의 포켓몬이 할 행동을 취합니다. 각 포켓몬의 행동 순서는
기본적으로 스피드 실수치가 높은쪽이 먼저 행동하게 됩니다. 하지만 우선도가 높은 기술을 사용하거나
짓궂은마음과 같이 우선도를 높여주는 특성을 가지고 있으면 먼저 행동할 수 있게 됩니다. 배틀 도중에
날씨나 필드가 생겨서 배틀중인 포켓몬이 영향을 받을 수 있습니다.
"""
from Player import Player, check_entry


# 배틀을 하기 전 체크해야 할 사항들을 체크합니다.
def prepare_for_single_battle(player1=Player, player2=Player):
    player1_number_of_pokemons = sum(pokemon is not None for pokemon in player1.entry)
    player2_number_of_pokemons = sum(pokemon is not None for pokemon in player2.entry)
    if (player1_number_of_pokemons < 3) | (player2_number_of_pokemons < 3):
        return -1
    else:
        player1_entry = check_entry(player1.entry)
        player2_entry = check_entry(player2.entry)
    if (player1_entry == -1) | (player2_entry == -1):
        return -1
    else:
        # 검증 완료
        return 1


# 배틀에 사용할 포켓몬을 정하는 함수. 싱글배틀이니 3마리를 선택한다.
# 6마리 미만의 엔트리에 대해서는 추후에 구현
def choose_pokemon_for_single_battle(player, indices):
    for index in indices:
        player.single_battle_entry.append(player.entry[index])


# 배틀에 사용할 포켓몬을 정하는 함수. 더블배틀이니 4마리를 선택한다.
# 6마리 미만의 엔트리에 대해서는 추후에 구현
def choose_pokemon_for_double_battle(player, indices):
    for index in indices:
        player.double_battle_entry.append(player.entry[index])


class PokemonBattle:
    def __init__(self, player1=Player, player2=Player, battle_type="Single"):
        self._player1 = player1
        self._player2 = player2
        self._player1_pokemon = None
        self._player2_pokemon = None
        self._battle_type = battle_type
        self._turn_count = 0
        self._weather = None
        self._field = None

    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player2

    @property
    def player1_pokemon(self):
        return self._player1_pokemon

    @property
    def player2_pokemon(self):
        return self._player2_pokemon

    @property
    def turn_count(self):
        return self._turn_count

    @player1.setter
    def player1(self, player):
        self._player1 = player

    @player2.setter
    def player2(self, player):
        self._player2 = player

    @player1_pokemon.setter
    def player1_pokemon(self, pokemon):
        self._player1_pokemon = pokemon

    @player2_pokemon.setter
    def player2_pokemon(self, pokemon):
        self._player2_pokemon = pokemon

    @turn_count.setter
    def turn_count(self, count):
        self._turn_count += count

    def SingleBattle(self):
        """
        싱글배틀은 다음과 같은 절차로 이루어집니다.
        1. 각 플레이어는 최소 3마리의 포켓몬을 준비합니다. 이때 3마리의 포켓몬은 다음 기준에 부합해야 합니다.
           - 각 포켓몬은 중복되어선 안된다.
           - 각 포켓몬이 지닌 물건이 모두 달라야 한다. 아무것도 지니지 않는 것은 상관없다.
        2. 각 플레이어는 3마리의 포켓몬을 원하는 순서로 준비합니다. 이때 첫번째 포켓몬이 선발로 나가게 됩니다.
        3. 게임이 시작되면 각자 선발 포켓몬을 꺼냅니다. 이때 포켓몬이 나오면서 사용되는 특성들이 처리됩니다.
           - 위협, 날씨특성, 긴장감, 통찰력, 불요의검 등의 특성등이 있습니다.
           - 양쪽 다 이러한 특성을 가지고 있을 경우, 스피드가 빠른 쪽의 특성이 먼저 적용됩니다. 스피드가 같다면
             50대 50으로 랜덤으로 순서가 정해집니다.
        4. 첫턴의 3번 처리 후 어떤 행동을 취할지 선택할 수 있습니다. 플레이어가 할 수 있는 행동은 다음과 같습니다.
           - 기술을 선택한다.
           - 포켓몬을 교체한다.
           - 항복한다.
        5. 양쪽이 어떤 행동을 취할지 결정이 끝나면 다음과 같은 상황들이 생깁니다.
           - 양쪽 모두 기술을 선택한 경우:
             양쪽 기술의 우선도를 확인합니다. 기술 자체의 우선도가 높을 수 있고 선제공격손톱이나 짓궂은마음 등으로 우선도가
             높을 수 있습니다. 우선도가 높은 쪽의 공격이 우선적으로 시행됩니다. 우선도가 동일할 경우 스피드가 빠른 포켓몬의
             기술이 먼저 나갑니다. 스피드가 같다면 50대 50으로 랜덤으로 순서가 정해집니다.
             한쪽 포켓몬이 공격해서 반대쪽 포켓몬의 HP를 0으로 만들었을 경우, 그 포켓몬은 기절상태가 되며 즉시 몬스터볼로
             돌아가게 됩니다. 기절한 포켓몬의 주인 플레이어는 해당 턴이 끝나면 다음턴으로 넘어가기 전에 다음 포켓몬을 꺼냅니다.
             만약 모든 포켓몬이 기절했다면 상대는 승리합니다.
             만약 선공 포켓몬이 추억의 선물, 자폭과 같은 기술을 사용해서 먼저 기절해 버린 경우, 그 포켓몬은 몬스터볼로 돌아가게
             됩니다. 하지만 아직 상대 포켓몬은 기술을 사용하지 않았기 때문에 우선 상대 포켓몬은 선택했던 기술을 사용합니다.
             그 후 턴이 종료되면 다음턴이 되기전에 기절한 쪽의 주인 플레이어는 다음 포켓몬을 꺼냅니다. 만약 전부 기절해 있다면
             상대 플레이어가 승리합니다.
           - 한쪽이 교체를 선책한 경우:
             교체가 먼저 시행됩니다. 포켓몬이 교체되고 만약 포켓몬이 나오면서 발동되는 특성이 있다면 그 즉시 발동됩니다.(위협 등)
             교체 행위가 끝난 뒤 상대방은 기술을 사용합니다.
             다만 예외적으로 따라가때리기를 사용했다면 우선 따라가때리기를 먼저 사용하고 그 후 포켓몬이 교체됩니다.
           - 양쪽이 교체를 선택한 경우:
             스피드가 빠른 쪽의 포켓몬이 우선 교체됩니다. 그리고 나오면서 발동되는 특성이 있다면 그 즉시 발동됩니다.
             처리가 끝난후 반대쪽의 포켓몬이 교체됩니다.
        :return:
        """
        # 각 플레이어의 엔트리를 점검합니다.
        prepare_for_single_battle(self.player1, self.player2)
        # 각 플레이어는 대전에 참여할 포켓몬 3마리를 고릅니다.
        choose_pokemon_for_single_battle(self.player1)
        choose_pokemon_for_single_battle(self.player2)

        # 각 플레이어는 첫번째 순서의 포켓몬을 꺼냅니다.
        self.player1_pokemon = self.player1.single_battle_entry[0]
        self.player2_pokemon = self.player2.single_battle_entry[0]


if __name__ == "__main__":
    lst = [0, 1, 2, 3, 4, 5, 6]

    print(lst[0])
