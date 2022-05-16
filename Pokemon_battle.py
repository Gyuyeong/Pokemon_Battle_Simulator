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
    def __init__(self, player1=Player, player2=Player):
        super().__init__(player1, player2)
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
    # 하나라도 잘못된게 있으면 -1을 반환한다.
    def check_entry(self):
        # 한 파티에 적어도 3마리의 포켓몬이 있는지 확인한다.
        if sum(pokemon is not None for pokemon in self.player1.entry) < 3:
            print("싱글배틀에 참여하기 위해서는 최소 3마리의 포켓몬을 준비해야 합니다.")
            return -1
        elif sum(pokemon is not None for pokemon in self.player2.entry) < 3:
            print("싱글배틀에 참여하기 위해서는 최소 3마리의 포켓몬을 준비해야 합니다.")
            return -1

        # 배틀에 참가할 1 플레이어부터 확인
        name_list = []
        item_list = []
        for pokemon in self.player1.entry:
            if pokemon is None:
                pass
            # 중복이 없는 경우
            elif pokemon.name not in name_list:
                name_list.append(pokemon.name)
            else:
                print("{}가 2마리 이상 엔트리에 포함되어 있습니다. 배틀에 참가하실 수 없습니다.".format(pokemon.name))
                return -1
        # 지닌물건 class 추후에 구현예정
        for pokemon in self.player1.entry:
            if pokemon is None:
                pass
            elif pokemon.held_item is None:
                pass
            elif pokemon.held_item not in item_list:
                item_list.append(pokemon.held_item)
            else:
                print("{}를 2마리 이상의 포켓몬이 지니고 있습니다. 배틀에 참가하실 수 없습니다.".format(pokemon.held_item))
                return -1
        
        # 배틀에 참가할 2 플레이어 확인
        name_list = []
        item_list = []
        for pokemon in self.player2.entry:
            if pokemon is None:
                pass
            # 중복이 없는 경우
            elif pokemon.name not in name_list:
                name_list.append(pokemon.name)
            else:
                print("{}가 2마리 이상 엔트리에 포함되어 있습니다. 배틀에 참가하실 수 없습니다.".format(pokemon.name))
                return -1
        # 지닌물건 class 추후에 구현예정
        for pokemon in self.player2.entry:
            if pokemon is None:
                pass
            elif pokemon.held_item is None:
                pass
            elif pokemon.held_item not in item_list:
                item_list.append(pokemon.held_item)
            else:
                print("{}를 2마리 이상의 포켓몬이 지니고 있습니다. 배틀에 참가하실 수 없습니다.".format(pokemon.held_item))
                return -1

        return 1

    # 대전에 내보낼 포켓몬을 고르기 전에 서로 어떤 포켓몬을 들고 왔는지 보여주는 과정
    def show_entry(self):
        print("Player 1 Entry")
        for number, pokemon in enumerate(self.player1.entry):
            if pokemon is None:
                pass
            else:
                print("{}. 이름: {}, 레벨: {}, 성별: {}".format(number + 1, pokemon.name, pokemon.level, pokemon.gender))

        print("=================================================")
        print("Player 2 Entry")
        for number, pokemon in enumerate(self.player2.entry):
            if pokemon is None:
                pass
            else:
                print("{}. 이름: {}, 레벨: {}, 성별: {}".format(number + 1, pokemon.name, pokemon.level, pokemon.gender))

    # 3마리의 포켓몬을 선택하는 과정입니다.
    def choose_pokemon_for_single_battle(self):
        # 1 플레이어가 한마리씩 선택한다.
        player1_indices = list()
        player1_indices.append(int(input("1 플레이어는 첫번째 포켓몬의 번호를 선택해주세요: ")) - 1)
        player1_indices.append(int(input("1 플레이어는 두번째 포켓몬의 번호를 선택해주세요: ")) - 1)
        player1_indices.append(int(input("1 플레이어는 세번째 포켓몬의 번호를 선택해주세요: ")) - 1)
        # 인덱스 중복 확인
        if len(set(player1_indices)) < 3:
            print("동일한 포켓몬을 중복으로 고를 수 없습니다.")
            return -1

        for index in player1_indices:
            # 없는 포켓몬번호을 고른 경우
            if index >= sum(pokemon is not None for pokemon in self.player1.entry):
                # 배틀에 나갈 3마리를 모두 비운다.
                player1.single_battle_entry.clear()
                print("인덱스 중 범위를 벗어나는 것이 있습니다. 수정해서 다시 제출하십쇼.")
                return -1
            else:
                player1.single_battle_entry.append(player1.entry[index])

        # 2 플레이어가 한마리씩 선택한다.
        player2_indices = list()
        player2_indices.append(int(input("2 플레이어는 첫번째 포켓몬의 번호를 선택해주세요: ")) - 1)
        player2_indices.append(int(input("2 플레이어는 두번째 포켓몬의 번호를 선택해주세요: ")) - 1)
        player2_indices.append(int(input("2 플레이어는 세번째 포켓몬의 번호를 선택해주세요: ")) - 1)
        # 인덱스 중복 확인
        if len(set(player2_indices)) < 3:
            print("동일한 포켓몬을 중복으로 고를 수 없습니다.")
            return -1

        for index in player2_indices:
            # 없는 포켓몬번호을 고른 경우
            if index >= sum(pokemon is not None for pokemon in self.player2.entry):
                # 배틀에 나갈 3마리를 모두 비운다.
                player2.single_battle_entry.clear()
                print("인덱스 중 범위를 벗어나는 것이 있습니다. 수정해서 다시 제출하십쇼.")
                return -1
            else:
                player2.single_battle_entry.append(player2.entry[index])

        return 1

    # 각 플레이어가 싱글배틀을 준비하게끔하는 함수이다.
    # check_entry, show_entry, choose_pokemon_for_single_battle 메소드를 통합한
    # 함수이다. 이 함수만 사용하면 엔트리 준비가 되게끔 했다.문제가 생기면 -1을 반환하고
    # 이상없으면 1을 반환한다.
    def get_ready_for_single_battle(self):
        checked_player = self.check_entry()
        # 체크를 했으나 문제가 있었음.
        if checked_player == -1:
            return -1

        self.show_entry()

        checked_battle_entry = self.choose_pokemon_for_single_battle()

        if checked_battle_entry == -1:
            return -1

        return 1


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

    battle = SingleBattle(player1=player1, player2=player2)
    battle.get_ready_for_single_battle()

    for pokemon in player1.single_battle_entry:
        print(pokemon.name)

    # battle.SingleBattle()
