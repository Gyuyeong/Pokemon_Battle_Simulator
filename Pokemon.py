"""
포켓몬이라는 class가 들어있는 파일입니다.
하나의 포켓몬에는 아주 많은 정보들이 들어있습니다.
이름, 성별, 기술, 기본 스텟, 개체값, 노력치 등
"""
from Pokemon_nature import PokemonNature
from Pokemon_nature import determine_nature_bonus


class Pokemon:
    """
    포켓몬 한마리에는 다음 정보들이 포함되어 있습니다.
    - 이름
    - 도감 번호
    - 타입 1, 2 (단일 타입은 Null_Type 으로 표기)
    - 특성 (1개만 있을 수 있음. 숨은 특성일 경우도 고려)
    - 성별 (수컷, 암컷, 무성 3가지가 존재한다.)
    - 성격 (성격마다 스텟에 보정이 들어갑니다.)
    - 교배 그룹
    - 키
    - 몸무게 (헤비봄버, 풀묶기 등의 기술들이 무게에 비례하여 데미지가 들어갑니다.)
    - 친밀도 (은혜갚기와 같이 친밀도 기반으로 위력이 정해지는 기술이 있다.)
    - 지닌물건 (지닌물건에 따라 여러가지가 변동될 수 있다.)
    - 종족값 (H:HP A:공격 B:방어 C:특수공격 D:특수방어 S:스피드) 실전은 레벨 50을 기준으로 합니다.
    - 노력치 (ev로 표현) (각 스텟마다 0 ~ 252까지이며 전체 스텟에 투자한 노력치는 512를 넘길 수 없습니다.)
    - 개체값 (iv로 표현) (각 스텟마다 0~31이다.)
    - 스텟 실수치 (종족값, 개체값, 노력치를 종합해서 나온 최종 수치. 이 수치를 기반으로 배틀이 진행됩니다.)
    - 기술 1,2,3,4
    - Z기술 여부 (Z기술 아이템을 지니고 있을 경우 활성화됩니다.) (추가 예정)
    - 진화 가능 여부 (진화의 휘석이라는 아이템의 존재로 중요합니다.)
    - 레벨 (보통 50으로 고정이나 가끔 일부로 레벨 1로 전략을 짜는 경우가 존재합니다.)
    - 각 스텟마다 랭크 상승 여부(각각 -6에서 6까지 가능)
    - 다이멕스 여부 
    - 거다이멕스 포켓몬 여부 (추가 예정)
    - 메가진화 여부 (해당하는 메가스톤을 지니고 있을 경우 활성화됩니다.) (추가 예정)
    - 상태이상 여부 (마비, 화상과 같은 주요 상태이상은 1개만 걸릴 수 있지만 풀이 죽는 등의 중복이 생길 수 있다.)
    - 전설 여부
    추후 추가예정...
    """

    def __init__(self, _name, _pokedex_number, _level,
                 _type1, _type2,
                 _ability, _gender, _nature, _egg_group,
                 _height, _weight,
                 _happiness,
                 _held_item,
                 _base_hp, _base_attack, _base_defense, _base_sp_attack, _base_sp_defense, _base_speed,
                 _iv_hp, _iv_attack, _iv_defense, _iv_sp_attack, _iv_sp_defense, _iv_speed,
                 _ev_hp, _ev_attack, _ev_defense, _ev_sp_attack, _ev_sp_defense, _ev_speed,
                 _move1, _move2, _move3, _move4,
                 _can_evolve,
                 _hp_rank, _attack_rank, _defense_rank, _sp_attack_rank, _sp_defense_rank, _speed_rank,
                 _evasiveness_rank, _accuracy_rank,
                 _is_dynamax,
                 _status_conditions,
                 _is_legendary):
        # 이름
        self._name = _name
        # 도감 번호
        self._pokedex_number = _pokedex_number
        # 레벨
        self._level = _level
        # 타입
        self._type1 = _type1
        self._type2 = _type2
        # 특성
        self._ability = _ability
        # 성별
        self._gender = _gender
        # 성격
        self._nature = _nature
        # 교배 그룹
        self._egg_group = _egg_group
        # 키, 몸무게
        self._height = _height
        self._weight = _weight
        # 친밀도
        self._happiness = _happiness
        # 지닌 물건
        self._held_item = _held_item
        # 종족값
        self._base_hp = _base_hp
        self._base_attack = _base_attack
        self._base_defense = _base_defense
        self._base_sp_attack = _base_sp_attack
        self._base_sp_defense = _base_sp_defense
        self._base_speed = _base_speed
        # 개체값
        self._iv_hp = _iv_hp
        self._iv_attack = _iv_attack
        self._iv_defense = _iv_defense
        self._iv_sp_attack = _iv_sp_attack
        self._iv_sp_defense = _iv_sp_defense
        self._iv_speed = _iv_speed
        # 노력치
        self._ev_hp = _ev_hp
        self._ev_attack = _ev_attack
        self._ev_defense = _ev_defense
        self._ev_sp_attack = _ev_sp_attack
        self._ev_sp_defense = _ev_sp_defense
        self._ev_speed = _ev_speed
        # 노력치의 총합은 512를 넘길 수 없다.
        self._ev_total = sum([self._ev_hp, self._ev_attack, self._ev_defense,
                              self._ev_sp_attack, self._ev_sp_defense, self._ev_sp_defense])
        # 실수치 계산
        # CalculateStats 함수는 아래에 있음. 클래스 합수로 구현됨.
        self._hp = self.CalculateStats(0)
        self._attack = self.CalculateStats(1)
        self._defense = self.CalculateStats(2)
        self._sp_attack = self.CalculateStats(3)
        self._sp_defense = self.CalculateStats(4)
        self._speed = self.CalculateStats(5)
        # 기술
        self._move1 = _move1
        self._move2 = _move2
        self._move3 = _move3
        self._move4 = _move4
        # 진화 여부
        self._can_evolve = _can_evolve
        # 랭크 변동
        self._hp_rank = 0
        self._attack_rank = 0
        self._defense_rank = 0
        self._sp_attack_rank = 0
        self._sp_defense_rank = 0
        self._speed_rank = 0
        self._evasiveness_rank = 0
        self._accuracy_rank = 0
        # 다이멕스 여부
        self._is_dynamax = _is_dynamax
        # 상태이상 여부
        self._status_conditions = _status_conditions
        # 전설 여부
        self._is_legendary = _is_legendary

    @property
    def name(self):
        return self._name

    @property
    def pokedex_number(self):
        return self._pokedex_number

    @property
    def level(self):
        return self._level

    @property
    def type1(self):
        return self._type1

    @property
    def type2(self):
        return self._type2

    @property
    def type(self):
        return self._type1, self._type2

    @property
    def ability(self):
        return self._ability

    @property
    def gender(self):
        return self._gender

    @property
    def nature(self):
        return self._nature

    @property
    def egg_group(self):
        return self._egg_group

    @property
    def height(self):
        return self._height

    @property
    def weight(self):
        return self._weight

    @property
    def happiness(self):
        return self._happiness

    @property
    def held_item(self):
        return self._held_item

    @property
    def base_hp(self):
        return self._base_hp

    @property
    def base_attack(self):
        return self._base_attack

    @property
    def base_defense(self):
        return self._base_defense

    @property
    def base_sp_attack(self):
        return self._base_sp_attack

    @property
    def base_sp_defense(self):
        return self._base_sp_defense

    @property
    def base_speed(self):
        return self._base_speed

    @property
    def iv_hp(self):
        return self._iv_hp

    @property
    def iv_attack(self):
        return self._iv_attack

    @property
    def iv_defense(self):
        return self._iv_defense

    @property
    def iv_sp_attack(self):
        return self._iv_sp_attack

    @property
    def iv_sp_defense(self):
        return self._iv_sp_defense

    @property
    def iv_speed(self):
        return self._iv_speed

    @property
    def ev_hp(self):
        return self._ev_hp

    @property
    def ev_attack(self):
        return self._ev_attack

    @property
    def ev_defense(self):
        return self._ev_defense

    @property
    def ev_sp_attack(self):
        return self._ev_sp_attack

    @property
    def ev_sp_defense(self):
        return self._ev_sp_defense

    @property
    def ev_speed(self):
        return self._ev_speed

    @property
    def ev_total(self):
        return self._ev_total

    @property
    def hp(self):
        return self._hp

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    @property
    def sp_attack(self):
        return self._sp_attack

    @property
    def sp_defense(self):
        return self._sp_defense

    @property
    def speed(self):
        return self._speed

    @property
    def move1(self):
        return self._move1

    @property
    def move2(self):
        return self._move2

    @property
    def move3(self):
        return self._move3

    @property
    def move4(self):
        return self._move4

    @property
    def moves(self):
        return self._move1, self._move2, self._move3, self._move4

    @property
    def can__evolve(self):
        return self._can_evolve

    @property
    def hp_rank(self):
        return self._hp_rank

    @property
    def attack_rank(self):
        return self._attack_rank

    @property
    def defense_rank(self):
        return self._defense_rank

    @property
    def sp_attack_rank(self):
        return self._sp_attack_rank

    @property
    def sp_defense_rank(self):
        return self._sp_defense_rank

    @property
    def speed_rank(self):
        return self._speed_rank

    @property
    def evasiveness_rank(self):
        return self._evasiveness_rank

    @property
    def accuracy_rank(self):
        return self._accuracy_rank

    @property
    def is_dynamax(self):
        return self._is_dynamax

    @property
    def status_conditions(self):
        return self._status_conditions

    @property
    def is_legendary(self):
        return self._is_legendary

    @level.setter
    def level(self, level=50):
        if level <= 0:
            raise ValueError("Level cannot be lower than 1.")
        elif level > 50:
            raise ValueError("Level cannot be higher than 50.")
        elif type(level) != int:
            raise TypeError("Level must be an integer value")
        self._level = level

    @type1.setter
    def type1(self, type1):
        self._type1 = type1

    @type2.setter
    def type2(self, type2):
        self._type2 = type2

    @ability.setter
    def ability(self, ability):
        self._ability = ability

    @nature.setter
    def nature(self, nature):
        self._nature = nature

    @egg_group.setter
    def egg_group(self, egg_group):
        self._egg_group = egg_group

    @height.setter
    def height(self, height):
        self._height = height

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @happiness.setter
    def happiness(self, happiness):
        if happiness < 0:
            raise ValueError("Happiness cannot be lower than 0.")
        elif happiness > 255:
            raise ValueError("Happiness cannot exceed 255.")
        elif type(happiness) != int:
            raise TypeError("Happiness value can only be an integer value.")
        self._happiness = happiness

    @held_item.setter
    def held_item(self, held_item):
        self._held_item = held_item

    @iv_hp.setter
    def iv_hp(self, hp):
        if hp < 0:
            raise ValueError("IV values cannot be lower than 0.")
        elif hp > 31:
            raise ValueError("IV values cannot be higher than 31.")
        elif type(hp) != int:
            raise TypeError("IV values must be an integer value.")
        self._iv_hp = hp
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.hp = self.CalculateStats(0)

    @iv_attack.setter
    def iv_attack(self, attack):
        if attack < 0:
            raise ValueError("IV values cannot be lower than 0.")
        elif attack > 31:
            raise ValueError("IV values cannot be higher than 31.")
        elif type(attack) != int:
            raise TypeError("IV values must be an integer value.")
        self._iv_attack = attack
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.attack = self.CalculateStats(1)

    @iv_defense.setter
    def iv_defense(self, defense):
        if defense < 0:
            raise ValueError("IV values cannot be lower than 0.")
        elif defense > 31:
            raise ValueError("IV values cannot be higher than 31.")
        elif type(defense) != int:
            raise TypeError("IV values must be an integer value.")
        self._iv_defense = defense
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.defense = self.CalculateStats(2)

    @iv_sp_attack.setter
    def iv_sp_attack(self, sp_attack):
        if sp_attack < 0:
            raise ValueError("IV values cannot be lower than 0.")
        elif sp_attack > 31:
            raise ValueError("IV values cannot be higher than 31.")
        elif type(sp_attack) != int:
            raise TypeError("IV values must be an integer value.")
        self._iv_sp_attack = sp_attack
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.sp_attack = self.CalculateStats(3)

    @iv_sp_defense.setter
    def iv_sp_defense(self, sp_defense):
        if sp_defense < 0:
            raise ValueError("IV values cannot be lower than 0.")
        elif sp_defense > 31:
            raise ValueError("IV values cannot be higher than 31.")
        elif type(sp_defense) != int:
            raise TypeError("IV values must be an integer value.")
        self._iv_sp_defense = sp_defense
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.sp_defense = self.CalculateStats(4)

    @iv_speed.setter
    def iv_speed(self, speed):
        if speed < 0:
            raise ValueError("IV values cannot be lower than 0.")
        elif speed > 31:
            raise ValueError("IV values cannot be higher than 31.")
        elif type(speed) != int:
            raise TypeError("IV values must be an integer value.")
        self._iv_speed = speed
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.speed = self.CalculateStats(5)

    @ev_hp.setter
    def ev_hp(self, hp=0):
        if hp < 0:
            raise ValueError("EV values cannot be lower than 0.")
        elif hp > 252:
            raise ValueError("EV values cannot be higher than 252.")
        elif type(hp) != int:
            raise TypeError("EV values must be an integer value.")
        elif self._ev_total + hp > 512:
            raise ValueError("Total EV cannot exceed 512.")
        self._ev_hp = hp
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.hp = self.CalculateStats(0)

    @ev_attack.setter
    def ev_attack(self, attack=0):
        if attack < 0:
            raise ValueError("EV values cannot be lower than 0.")
        elif attack > 252:
            raise ValueError("EV values cannot be higher than 252.")
        elif type(attack) != int:
            raise TypeError("EV values must be an integer value.")
        elif self._ev_total + attack > 512:
            raise ValueError("Total EV cannot exceed 512.")
        self._ev_attack = attack
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.attack = self.CalculateStats(1)

    @ev_defense.setter
    def ev_defense(self, defense=0):
        if defense < 0:
            raise ValueError("EV values cannot be lower than 0.")
        elif defense > 252:
            raise ValueError("EV values cannot be higher than 252.")
        elif type(defense) != int:
            raise TypeError("EV values must be an integer value.")
        elif self._ev_total + defense > 512:
            raise ValueError("Total EV cannot exceed 512.")
        self._ev_defense = defense
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.defense = self.CalculateStats(2)

    @ev_sp_attack.setter
    def ev_sp_attack(self, sp_attack=0):
        if sp_attack < 0:
            raise ValueError("EV values cannot be lower than 0.")
        elif sp_attack > 252:
            raise ValueError("EV values cannot be higher than 252.")
        elif type(sp_attack) != int:
            raise TypeError("EV values must be an integer value.")
        elif self._ev_total + sp_attack > 512:
            raise ValueError("Total EV cannot exceed 512.")
        self._ev_sp_attack = sp_attack
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.sp_attack = self.CalculateStats(3)

    @ev_sp_defense.setter
    def ev_sp_defense(self, sp_defense=0):
        if sp_defense < 0:
            raise ValueError("EV values cannot be lower than 0.")
        elif sp_defense > 252:
            raise ValueError("EV values cannot be higher than 252.")
        elif type(sp_defense) != int:
            raise TypeError("EV values must be an integer value.")
        elif self._ev_total + sp_defense > 512:
            raise ValueError("Total EV cannot exceed 512.")
        self._ev_sp_defense = sp_defense
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.sp_defense = self.CalculateStats(4)

    @ev_speed.setter
    def ev_speed(self, speed=0):
        if speed < 0:
            raise ValueError("EV values cannot be lower than 0.")
        elif speed > 252:
            raise ValueError("EV values cannot be higher than 252.")
        elif type(speed) != int:
            raise TypeError("EV values must be an integer value.")
        elif self._ev_total + speed > 512:
            raise ValueError("Total EV cannot exceed 512.")
        self._ev_speed = speed
        # 노력치와 개체값에 변동이 생기면 다시 실수치를 계산한다.
        self.speed = self.CalculateStats(5)

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @attack.setter
    def attack(self, attack):
        self._attack = attack

    @defense.setter
    def defense(self, defense):
        self._defense = defense

    @sp_attack.setter
    def sp_attack(self, sp_attack):
        self._sp_attack = sp_attack

    @sp_defense.setter
    def sp_defense(self, sp_defense):
        self._sp_defense = sp_defense

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    # 기술 추가시 중복을 확인해야 함. 추후 구현
    @move1.setter
    def move1(self, move):
        self._move1 = move

    @move2.setter
    def move2(self, move):
        self._move2 = move

    @move3.setter
    def move3(self, move):
        self._move3 = move

    @move4.setter
    def move4(self, move):
        self._move4 = move
            
    @is_dynamax.setter
    def is_dynamax(self, is_dynamax=False):
        self._is_dynamax = is_dynamax
            
    # 일반 전설과 초전설도 구분해야 함. 추후 구현
    @is_legendary.setter
    def is_legendary(self, is_legendary=False):
        self._is_legendary = is_legendary

    # 실수치 계산. (성격보정은 추후 구현 예정)
    # self._hp = int(self._base_hp + (self._iv_hp/2) + (self._ev_hp/8) + 10 + 50)
    # self._attack = int((self._base_attack + (_iv_attack/2) + (_ev_attack/8) + 5)*(성격보정))
    # self._defense = int((self._base_defense + (_iv_defense/2) + (_ev_defense/8) + 5)*(성격보정))
    # self._sp_attack = int((self._base_sp_attack + (_iv_sp_attack/2) + (_ev_sp_attack/8) + 5)*(성격보정))
    # self._sp_defense = int((self._base_sp_defense + (_iv_sp_defense/2) + (_ev_sp_defense/8) + 5)*(성격보정))
    # self._speed = int((self._base_speed + (_iv_speed/2) + (_ev_speed/8) + 5)*(성격보정))
    
    # 실수치 계산 함수
    def CalculateStats(self, stat_index):
        """

        :param stat_index: 0: hp, 1: attack, 2: defense, 3: sp_attack, 4: sp_defense, 5: speed
        :return: 실수치
        """
        nature = self._nature
        boost_stat, reduce_stat = determine_nature_bonus(nature)
        # hp 실수치
        if stat_index == 0:
            hp_stat = int(self._base_hp + (self._iv_hp/2) + (self._ev_hp/8) + 10 + 50)
            return hp_stat
        # 공격 실수치
        elif stat_index == 1:
            if boost_stat == 1:
                attack_stat = int((self._base_attack + (self._iv_attack/2) + (self._ev_attack/8) + 5)*1.1)
            elif reduce_stat == 1:
                attack_stat = int((self._base_attack + (self._iv_attack/2) + (self._ev_attack/8) + 5)*0.9)
            else:
                attack_stat = int((self._base_attack + (self._iv_attack/2) + (self._ev_attack/8) + 5))
            return attack_stat
        # 방어 실수치
        elif stat_index == 2:
            if boost_stat == 2:
                defense_stat = int((self._base_defense + (self._iv_defense/2) + (self._ev_defense/8) + 5)*1.1)
            elif reduce_stat == 2:
                defense_stat = int((self._base_defense + (self._iv_defense/2) + (self._ev_defense/8) + 5)*0.9)
            else:
                defense_stat = int((self._base_defense + (self._iv_defense/2) + (self._ev_defense/8) + 5))
            return defense_stat
        # 특공 실수치
        elif stat_index == 3:
            if boost_stat == 3:
                sp_attack_stat = int((self._base_sp_attack + (self._iv_sp_attack/2) + (self._ev_sp_attack/8) + 5)*1.1)
            elif reduce_stat == 3:
                sp_attack_stat = int((self._base_sp_attack + (self._iv_sp_attack/2) + (self._ev_sp_attack/8) + 5)*0.9)
            else:
                sp_attack_stat = int((self._base_sp_attack + (self._iv_sp_attack/2) + (self._ev_sp_attack/8) + 5))
            return sp_attack_stat
        # 특방 실수치
        elif stat_index == 4:
            if boost_stat == 4:
                sp_defense_stat = int((self._base_sp_defense + (self._iv_sp_defense/2) + (self._ev_sp_defense/8) + 5)*1.1)
            elif reduce_stat == 4:
                sp_defense_stat = int((self._base_sp_defense + (self._iv_sp_defense/2) + (self._ev_sp_defense/8) + 5)*0.9)
            else:
                sp_defense_stat = int((self._base_sp_defense + (self._iv_sp_defense/2) + (self._ev_sp_defense/8) + 5))
            return sp_defense_stat
        # 스피드 실수치
        elif stat_index == 5:
            if boost_stat == 5:
                speed_stat = int((self._base_speed + (self._iv_speed/2) + (self._ev_speed/8) + 5)*1.1)
            elif reduce_stat == 5:
                speed_stat = int((self._base_speed + (self._iv_speed/2) + (self._ev_speed/8) + 5)*0.9)
            else:
                speed_stat = int((self._base_speed + (self._iv_speed/2) + (self._ev_speed/8) + 5))
            return speed_stat


if __name__ == "__main__":
    squirtle = Pokemon("Squirtle", 7, 50, "water", "None", "Torrent", "Male", PokemonNature.BASHFUL, "Monster",
                       0.5, 1.08, 50, "None", 44, 48, 65, 50, 64, 43, 31, 31, 31, 31, 31, 31, 252, 0, 252, 0, 4, 0,
                       "None", "None", "None", "None", True, 0, 0, 0, 0, 0, 0, 0, 0, False, "None", False)
    print("HP: " + str(squirtle.hp))
    print("공격: " + str(squirtle.attack))
    print("방어: " + str(squirtle.defense))
    print("특공: " + str(squirtle.sp_attack))
    print("특방: " + str(squirtle.sp_defense))
    print("스피드: " + str(squirtle.speed))
    print("\n")
    print("방어 노력치: " + str(squirtle.ev_defense))

    squirtle.ev_defense = 0

    print("방어 노력치 변동 후: " + str(squirtle.ev_defense))
    print("방어 변동결과: " + str(squirtle.defense))