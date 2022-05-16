"""
포켓몬 배틀에 관한 파일입니다. 배틀을 하나의 클래스로 만들어서 각 배틀을 개체로 만들어봅니다.
포켓몬은 턴제 게임입니다.양쪽이 매턴 자신의 포켓몬이 할 행동을 취합니다. 각 포켓몬의 행동 순서는
기본적으로 스피드 실수치가 높은쪽이 먼저 행동하게 됩니다. 하지만 우선도가 높은 기술을 사용하거나
짓궂은마음과 같이 우선도를 높여주는 특성을 가지고 있으면 먼저 행동할 수 있게 됩니다. 배틀 도중에
날씨나 필드가 생겨서 배틀중인 포켓몬이 영향을 받을 수 있습니다.
"""
from Player import Player
from Pokemon import Pokemon
from Pokemon_nature import PokemonNature
from Pokemon_type import PokemonType


class PokemonBattle:
    def __init__(self, player1=Player, player2=Player):
        self._player1 = player1
        self._player2 = player2
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
    def turn_count(self):
        return self._turn_count

    @player1.setter
    def player1(self, player):
        self._player1 = player

    @player2.setter
    def player2(self, player):
        self._player2 = player

    @turn_count.setter
    def turn_count(self, count):
        self._turn_count += count


class SingleBattle(PokemonBattle):
    def __init__(self):
        super().__init__()
        self._player1_pokemon = None
        self._player2_pokemon = None

    @property
    def player1_pokemon(self):
        return self._player1_pokemon

    @property
    def player2_pokemon(self):
        return self._player2_pokemon

    @player1_pokemon.setter
    def player1_pokemon(self, pokemon):
        self._player1_pokemon = pokemon

    @player2_pokemon.setter
    def player2_pokemon(self, pokemon):
        self._player2_pokemon = pokemon
        
    # ====================================================================
    # 여기서부터 다시 생각하고 구현해야함.
    # 엔트리가 기준에 부합하는지 확인하는 함수
    def check_entry(self, entry):
        name_list = []
        item_list = []
        for pokemon in entry:
            if pokemon is None:
                pass
            # 중복이 없는 경우
            elif pokemon.name not in name_list:
                name_list.append(pokemon.name)
            else:
                print("{}가 2마리 이상 엔트리에 포함되어 있습니다. 배틀에 참가하실 수 없습니다.".format(pokemon.name))
                return -1
        # 지닌물건 class 추후에 구현예정
        for pokemon in entry:
            if pokemon is None:
                pass
            elif pokemon.held_item is None:
                pass
            elif pokemon.held_item not in item_list:
                item_list.append(pokemon.held_item)
            else:
                print("{}를 2마리 이상의 포켓몬이 지니고 있습니다. 배틀에 참가하실 수 없습니다.".format(pokemon.held_item))
                return -1

        return entry

    # 배틀을 하기 전 체크해야 할 사항들을 체크합니다.
    def prepare_for_single_battle(self, player=Player):
        player_number_of_pokemons = sum(pokemon is not None for pokemon in player.entry)
        if player_number_of_pokemons < 3:
            return -1
        else:
            player_entry = self.check_entry(player.entry)
        if player_entry == -1:
            return -1
        else:
            # 검증 완료 (최소 3마리 이상의 포켓몬이 엔트리에 있고 모두 기준에 합당함.)
            return 1

    def choose_pokemon_for_single_battle(self, player, indices):
        # 인덱스 중복 확인
        if len(set(indices)) < 3:
            print("동일한 포켓몬을 중복으로 고를 수 없습니다.")
            return -1

        for index in indices:
            # 없는 포켓몬칸을 고른 경우
            if index >= sum(pokemon is not None for pokemon in player.entry):
                # 배틀에 나갈 3마리를 모두 비운다.
                player.single_battle_entry.clear()
                print("인덱스 중 범위를 벗어나는 것이 있습니다. 수정해서 다시 제출하십쇼.")
                return -1
            else:
                player.single_battle_entry.append(player.entry[index])

    # 각 플레이어가 싱글배틀을 준비하게끔하는 함수이다. 각 플레이어마다 따로 분리해놔야 한다고 생각했다.
    def get_ready_for_single_battle(self, player, indices):
        checked_player = self.prepare_for_single_battle(player)
        # 체크를 했으나 문제가 있었음.
        if checked_player == -1:
            return -1

        checked_battle_entry = self.choose_pokemon_for_single_battle(player, indices)
        if checked_battle_entry == -1:
            return -1
        return 1

    # 6마리 엔트리를 상대에게 보여주는 작업이다.
    def show_entry(self, player=Player):
        for number, pokemon in enumerate(player.entry):
            if pokemon is None:
                pass
            else:
                print("{}. 이름: {}, 레벨: {}, 성별: {}".format(number + 1, pokemon.name, pokemon.level, pokemon.gender))

    # def SingleBattle(self):
    #     """
    #     싱글배틀은 다음과 같은 절차로 이루어집니다.
    #     1. 각 플레이어는 최소 3마리의 포켓몬을 준비합니다. 이때 3마리의 포켓몬은 다음 기준에 부합해야 합니다.
    #        - 각 포켓몬은 중복되어선 안된다.
    #        - 각 포켓몬이 지닌 물건이 모두 달라야 한다. 아무것도 지니지 않는 것은 상관없다.
    #     2. 각 플레이어는 3마리의 포켓몬을 원하는 순서로 준비합니다. 이때 첫번째 포켓몬이 선발로 나가게 됩니다.
    #     3. 게임이 시작되면 각자 선발 포켓몬을 꺼냅니다. 이때 포켓몬이 나오면서 사용되는 특성들이 처리됩니다.
    #        - 위협, 날씨특성, 긴장감, 통찰력, 불요의검 등의 특성등이 있습니다.
    #        - 양쪽 다 이러한 특성을 가지고 있을 경우, 스피드가 빠른 쪽의 특성이 먼저 적용됩니다. 스피드가 같다면
    #          50대 50으로 랜덤으로 순서가 정해집니다.
    #     4. 첫턴의 3번 처리 후 어떤 행동을 취할지 선택할 수 있습니다. 플레이어가 할 수 있는 행동은 다음과 같습니다.
    #        - 기술을 선택한다.
    #        - 포켓몬을 교체한다.
    #        - 항복한다.
    #     5. 양쪽이 어떤 행동을 취할지 결정이 끝나면 다음과 같은 상황들이 생깁니다.
    #        - 양쪽 모두 기술을 선택한 경우:
    #          양쪽 기술의 우선도를 확인합니다. 기술 자체의 우선도가 높을 수 있고 선제공격손톱이나 짓궂은마음 등으로 우선도가
    #          높을 수 있습니다. 우선도가 높은 쪽의 공격이 우선적으로 시행됩니다. 우선도가 동일할 경우 스피드가 빠른 포켓몬의
    #          기술이 먼저 나갑니다. 스피드가 같다면 50대 50으로 랜덤으로 순서가 정해집니다.
    #          한쪽 포켓몬이 공격해서 반대쪽 포켓몬의 HP를 0으로 만들었을 경우, 그 포켓몬은 기절상태가 되며 즉시 몬스터볼로
    #          돌아가게 됩니다. 기절한 포켓몬의 주인 플레이어는 해당 턴이 끝나면 다음턴으로 넘어가기 전에 다음 포켓몬을 꺼냅니다.
    #          만약 모든 포켓몬이 기절했다면 상대는 승리합니다.
    #          만약 선공 포켓몬이 추억의 선물, 자폭과 같은 기술을 사용해서 먼저 기절해 버린 경우, 그 포켓몬은 몬스터볼로 돌아가게
    #          됩니다. 하지만 아직 상대 포켓몬은 기술을 사용하지 않았기 때문에 우선 상대 포켓몬은 선택했던 기술을 사용합니다.
    #          그 후 턴이 종료되면 다음턴이 되기전에 기절한 쪽의 주인 플레이어는 다음 포켓몬을 꺼냅니다. 만약 전부 기절해 있다면
    #          상대 플레이어가 승리합니다.
    #        - 한쪽이 교체를 선책한 경우:
    #          교체가 먼저 시행됩니다. 포켓몬이 교체되고 만약 포켓몬이 나오면서 발동되는 특성이 있다면 그 즉시 발동됩니다.(위협 등)
    #          교체 행위가 끝난 뒤 상대방은 기술을 사용합니다.
    #          다만 예외적으로 따라가때리기를 사용했다면 우선 따라가때리기를 먼저 사용하고 그 후 포켓몬이 교체됩니다.
    #        - 양쪽이 교체를 선택한 경우:
    #          스피드가 빠른 쪽의 포켓몬이 우선 교체됩니다. 그리고 나오면서 발동되는 특성이 있다면 그 즉시 발동됩니다.
    #          처리가 끝난후 반대쪽의 포켓몬이 교체됩니다.
    #     :return:
    #     """
    #     # 배틀에 참가할 포켓몬들을 서로 보여주고 이중 3마리를 고릅니다.
    #     print("Player 1 엔트리")
    #     show_entry(player1)
    #     print("===============================================")
    #     print("Player2 엔트리")
    #     show_entry(player2)
    #
    #     checked_result1 = get_ready_for_single_battle(player1, [0, 3, 4])
    #     checked_result2 = get_ready_for_single_battle(player2, [1, 4, 3])
    #
    #     if (checked_result1 == -1) | (checked_result2 == -1):
    #         return -1
    #
    #
    #     # 각 플레이어는 첫번째 순서의 포켓몬을 꺼냅니다.
    #     self.player1_pokemon = self.player1.single_battle_entry[0]
    #     self.player2_pokemon = self.player2.single_battle_entry[0]
    #
    #     print(self.player1_pokemon.name)
    #     print(self.player2_pokemon.name)


if __name__ == "__main__":
    pokemon1 = Pokemon("Squirtle", 7, 50, PokemonType.WATER, "None", "Torrent", "Male", PokemonNature.BASHFUL,
                       "Monster",
                       0.5, 9, 50, None, 44, 48, 65, 50, 64, 43, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                       "None", "None", "None", "None", True, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", False)

    pokemon2 = Pokemon("Pikachu", 25, 50, PokemonType.ELECTRIC, "None", "Static", "Male", PokemonNature.MODEST, "Monster",
                       0.4, 6, 50, None, 35, 55, 40, 50, 50, 90, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                       "None", "None", "None", "None", True, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", False)

    pokemon3 = Pokemon("Dragonite", 149, 50, PokemonType.DRAGON, PokemonType.FLYING, "Multiscale", "Male", PokemonNature.JOLLY, "Monster",
                       2.2, 210, 50, None, 91, 134, 95, 100, 100, 80, 31, 31, 31, 31, 31, 31, 0, 0, 252, 0, 4, 252,
                       "None", "None", "None", "None", False, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", False)

    pokemon4 = Pokemon("Dialga", 483, 50, PokemonType.STEEL, PokemonType.DRAGON, "Pressure", "Unknown", PokemonNature.BOLD, "Monster",
                       7, 850, 50, None, 100, 120, 120, 150, 100, 90, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                       "None", "None", "None", "None", False, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", True)

    pokemon5 = Pokemon("Swampert", 260, 50, PokemonType.WATER, PokemonType.GROUND, "Torrent", "Male", PokemonNature.BOLD, "Monster",
                       1.5, 81.9, 50, None, 100, 110, 90, 85, 90, 60, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                       "None", "None", "None", "None", False, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", False)

    pokemon6 = Pokemon("Zacian", 888, 50, PokemonType.FAIRY, PokemonType.STEEL, "Intrepid_Sword", "Unknown", PokemonNature.JOLLY, "Monster",
                       2.8, 110, 50, "Crowned_Sword", 92, 170, 115, 80, 115, 148, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                       "None", "None", "None", "None", False, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", True)

    pokemon7 = Pokemon("Squirtle", 7, 50, PokemonType.WATER, "None", "Torrent", "Male", PokemonNature.SASSY, "Monster",
                       0.5, 9, 50, None, 44, 48, 65, 50, 64, 43, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                       "None", "None", "None", "None", True, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", False)

    pokemon8 = Pokemon("Palkia", 484, 50, PokemonType.WATER, PokemonType.DRAGON, "Pressure", "Unknown", PokemonNature.JOLLY, "Monster",
                       6.3, 660, 50, None, 90, 120, 100, 150, 120, 100, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                       "None", "None", "None", "None", False, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", True)

    pokemon9 = Pokemon("Geodude", 74, 50, PokemonType.ROCK, PokemonType.GROUND, "Sturdy", "Male", PokemonNature.LAX, "Monster",
                       0.4, 20, 50, None, 40, 80, 100, 30, 30, 20, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                       "None", "None", "None", "None", True, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", False)

    pokemon10 = Pokemon("Lugia", 249, 50, PokemonType.PSYCHIC, PokemonType.FLYING, "Multiscale", "Unknown", PokemonNature.CALM, "Monster",
                        5.2, 216, 50, None, 106, 90, 130, 90, 154, 110, 31, 31, 31, 31, 31, 31, 4, 0, 0, 0, 252, 252,
                        "None", "None", "None", "None", False, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", True)

    pokemon11 = Pokemon("Kangaskhan", 115, 50, PokemonType.NORMAL, "None", "Inner_Focus", "Male", PokemonNature.ADAMANT, "Monster",
                        2.2, 80, 50, None, 105, 95, 80, 40, 80, 90, 31, 31, 31, 31, 31, 31, 0, 252, 0, 0, 4, 252,
                        "None", "None", "None", "None", False, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", False)

    pokemon12 = Pokemon("Tapu_Fini", 788, 50, PokemonType.WATER, PokemonType.FAIRY, "Misty_Surge", "Unknown", PokemonNature.CALM, "Monster",
                        1.3, 21.2, 50, None, 70, 75, 115, 95, 130, 85, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                        "None", "None", "None", "None", False, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", True)

    player1 = Player(pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6)
    player2 = Player(pokemon7, pokemon8, pokemon9, pokemon10, pokemon11, pokemon12)

    battle = PokemonBattle(player1, player2)

    # battle.SingleBattle()
