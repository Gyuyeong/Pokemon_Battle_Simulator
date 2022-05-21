"""
Uses Selenium to fetch pokemon data and save it in a pandas dataframe.
"""
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs

import re



def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


def get_number_of_pokemons_by_alphabet(alphabet):
    if alphabet == "A" or alphabet == 'a':
        return 40
    elif alphabet == "B" or alphabet == 'b':
        return 49
    elif alphabet == "C" or alphabet == 'c':
        return 76
    elif alphabet == "D" or alphabet == 'd':
        return 56
    elif alphabet == "E" or alphabet == 'e':
        return 25
    elif alphabet == "F" or alphabet == 'f':
        return 31
    elif alphabet == "G" or alphabet == 'g':
        return 57
    elif alphabet == "H" or alphabet == 'h':
        return 32
    elif alphabet == "I" or alphabet == 'i':
        return 9
    elif alphabet == "J" or alphabet == 'j':
        return 8
    elif alphabet == "K" or alphabet == 'k':
        return 28
    elif alphabet == "L" or alphabet == 'l':
        return 38
    elif alphabet == "M" or alphabet == 'm':
        return 73
    elif alphabet == "N" or alphabet == "n":
        return 20
    elif alphabet == "O" or alphabet == 'o':
        return 11
    elif alphabet == "P" or alphabet == 'p':
        return 59
    elif alphabet == "Q" or alphabet == 'q':
        return 5
    elif alphabet == "R" or alphabet == 'r':
        return 35
    elif alphabet == "S" or alphabet == 's':
        return 125
    elif alphabet == "T" or alphabet == 't':
        return 53
    elif alphabet == "U" or alphabet == 'u':
        return 7
    elif alphabet == "V" or alphabet == 'v':
        return 23
    elif alphabet == "W" or alphabet == 'w':
        return 25
    elif alphabet == "X" or alphabet == 'x':
        return 3
    elif alphabet == "Y" or alphabet == 'y':
        return 6
    elif alphabet == "Z" or alphabet == 'z':
        return 14


URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name"

driver = set_chrome_driver()
driver.get(url=URL)


def find_tags_without_certain_attribute(tag):
    return tag.has_attr("width") and not tag.has_attr('display')


alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

num = 0
# 포켓몬들을 넣을 리스트
pokemons = list()

for alphabet in alphabet_list:
    number_of_pokemons_by_alphabet = get_number_of_pokemons_by_alphabet(alphabet)
    timeout = 5

    for number in range(number_of_pokemons_by_alphabet):
        # 개별 포켓몬의 정보를 저장할 dictionary 만들기
        pokemon = dict()
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div/table[{}]/tbody/tr[{}]/td[2]/a'.format(num + 1, number + 2)))
        # WebDriverWait(driver, timeout).until(element_present)
        # 목록에서 찾고 클릭
        element = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div/table[{}]/tbody/tr[{}]/td[2]/a'.format(num + 1, number + 2))
        element.click()

        # 개별 포켓몬 사이트호 이동함.
        page_html = driver.page_source
        soup = bs(page_html, 'html.parser')

        # 이름, 도감번호, 타입, 교배그룹, 키, 몸무게가 들어있는 테이블이다.
        information_table = soup.findAll("table", style=re.compile(r'float:right; text-align:center; width:33%; max-width:420px;.*?padding:2px;'))[0]
        # 종족값이 들어있는 테이블
        stats_table = soup.findAll("table", style=re.compile(r'.*?border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; border:.*?white-space:nowrap'))
        # 2개 이상 있는 경우는 메가진화와 같이 종족값에 변화가 생기는 경우이다.
        print(len(stats_table))
        # 한글 이름이 들어있는 테이블
        name_table = soup.findAll("table", {"class": "roundy"}, style=re.compile(r'background:.*?; border: 3px solid.*?; float:left'))[0]
        
        # 포켓몬 정보를 추출해내는 과정:
        # 포켓몬 이름
        name = information_table.find("td", {"width": "75%", "class": "roundy", "style": "background:#FFF;"}).find("b").string
        # 도감 번호
        pokedex_number = int(information_table.find("th", {"width": "25%", "class": "roundy", "style": "background:#FFF;"}).find("span").string[1:])
        # 타입을 담을 리스트
        pokemon_types = list()
        # 타입을 추출해내는 과정
        for table in information_table.findAll("td", {"class": "roundy", "colspan": "2"}, style=re.compile(r'background:.*?; padding:2px;')):
            # Type이 들어있는 테이블인지 확인
            if table.find("a").find("span").string == "Type":
                # Display: None인 td들을 거르는 작업
                type_td = table.findAll(lambda tag: tag.name == "td" and not tag.attrs)[0]
                types = type_td.findAll("b")
                # 단일 타입의 경우
                if len(types) == 1:
                    pokemon_types.append(types[0].string)
                    pokemon_types.append("None")
                # 타입이 세개 이상 적혀있는 경우가 있음. 이점을 처리해야 함. (자시안처럼 따로 적혀있는 경우)
                else:
                    for t in types:
                        pokemon_types.append(t.string)

        # 특성 추출과정
        tds = information_table.findAll("td", {"class": "roundy", "colspan": "2"})
        for td in tds:
            try:
                if td.find("a").find("span").string == "Abilities":
                    ability_tds = td.findAll(lambda tag: tag.has_attr("width") and not tag.has_attr("style"))
                    for ability_td in ability_tds:
                        print(ability_td)
            except:
                pass
            # print(td)
            # print("=========================================")

        # # 교배그룹 추출과정
        # tds = information_table.findAll("td", {"width": "50%"})
        # for td in tds:
        #     print(td)

        # print(soup.findAll("td"))
        # for td in soup.findAll("td"):
        #     if ("colspan" in td.attrs) and (td.attrs["colspan"] == "2"):
        #         print(td)
        #         print("===================================================")
        # print(soup)

        # # 이름, 도감번호, 타입 등이 있는 중요한 테이블이다.
        # main_tbody = soup.findAll("table")[4].findAll("tbody")[0]  # 리스트로 나와서 빼줌.
        # # for tr in main_tbody.findAll("tr"):
        # #     print(tr)
        # #     print("==========================================")
        # # 영문 이름
        # name = main_tbody.findAll("tr")[2].find("td").find("b").string
        # # 포켓몬 타입 추출
        # pokemon_types = list()
        # for pokemon_type in main_tbody.findAll("tr")[10].findAll("b"):
        #     pokemon_types.append(pokemon_type.string)
        #
        # # 교배 그룹
        # pokemon_egg_groups = list()
        # for egg_group in main_tbody.findAll("tr")[25].findAll("span"):
        #     pokemon_egg_groups.append(egg_group.string)

        # # 키
        # height = main_tbody.findAll("tr")[28].findAll("td")[1].string
        #
        # print(main_tbody.findAll("tr")[35])

        # main_tbody.findAll[10] # 타입이 들어있음.
        # main_tbody.findAll[17] # 특성 들어있음.
        # main_tbody.findAll[25] # 교배 그룹 들어있음.
        # main_tbody.findAll[27] # 키 몸무게 들어있음.



        driver.back()
        WebDriverWait(driver, timeout).until(element_present)
        break
    num += 1
    break



# A
'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td[2]/a'
'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[3]/td[2]/a'
'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[4]/td[2]/a'
'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[41]/td[2]/a'
# B
'//*[@id="mw-content-text"]/div/table[2]/tbody/tr[2]/td[2]/a'
'//*[@id="mw-content-text"]/div/table[2]/tbody/tr[50]/td[2]/a'

# C
'//*[@id="mw-content-text"]/div/table[3]/tbody/tr[2]/td[2]/a'
'//*[@id="mw-content-text"]/div/table[3]/tbody/tr[77]/td[2]/a'

# D
'//*[@id="mw-content-text"]/div/table[4]/tbody/tr[57]/td[2]/a'

# E
'//*[@id="mw-content-text"]/div/table[5]/tbody/tr[26]/td[2]/a'

# F
'//*[@id="mw-content-text"]/div/table[6]/tbody/tr[32]/td[2]/a'

# G
'//*[@id="mw-content-text"]/div/table[7]/tbody/tr[58]/td[2]/a'

# H
'//*[@id="mw-content-text"]/div/table[8]/tbody/tr[33]/td[2]/a'

# I
'//*[@id="mw-content-text"]/div/table[9]/tbody/tr[10]/td[2]/a'

# J
'//*[@id="mw-content-text"]/div/table[10]/tbody/tr[9]/td[2]/a'

# K
'//*[@id="mw-content-text"]/div/table[11]/tbody/tr[29]/td[2]/a'

# L
'//*[@id="mw-content-text"]/div/table[12]/tbody/tr[39]/td[2]/a'

# M
'//*[@id="mw-content-text"]/div/table[13]/tbody/tr[74]/td[2]/a'

# N
'//*[@id="mw-content-text"]/div/table[14]/tbody/tr[21]/td[2]/a'

# O
'//*[@id="mw-content-text"]/div/table[15]/tbody/tr[12]/td[2]/a'

# P
'//*[@id="mw-content-text"]/div/table[16]/tbody/tr[60]/td[2]/a'

# Q
'//*[@id="mw-content-text"]/div/table[17]/tbody/tr[6]/td[2]/a'

# R
'//*[@id="mw-content-text"]/div/table[18]/tbody/tr[36]/td[2]/a'

# S
'//*[@id="mw-content-text"]/div/table[19]/tbody/tr[126]/td[2]/a'

# T
'//*[@id="mw-content-text"]/div/table[20]/tbody/tr[54]/td[2]/a'

# U
'//*[@id="mw-content-text"]/div/table[21]/tbody/tr[8]/td[2]/a'

# V
'//*[@id="mw-content-text"]/div/table[22]/tbody/tr[24]/td[2]/a'

# W
'//*[@id="mw-content-text"]/div/table[23]/tbody/tr[26]/td[2]/a'

# X
'//*[@id="mw-content-text"]/div/table[24]/tbody/tr[4]/td[2]/a'

# Y
'//*[@id="mw-content-text"]/div/table[25]/tbody/tr[7]/td[2]/a'

# Z
'//*[@id="mw-content-text"]/div/table[26]/tbody/tr[15]/td[2]/a'
