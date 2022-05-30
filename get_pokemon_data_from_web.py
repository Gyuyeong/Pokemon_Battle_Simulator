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

import pandas as pd
import numpy as np


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

# for number in range(get_number_of_pokemons_by_alphabet("f")):
#     # 개별 포켓몬의 정보를 저장할 dictionary 만들기
#     pokemon = dict()
#     element_present = EC.presence_of_element_located(
#         (By.XPATH, '//*[@id="mw-content-text"]/div/table[{}]/tbody/tr[{}]/td[2]/a'.format(6, number + 2)))
#     # WebDriverWait(driver, timeout).until(element_present)
#     # 목록에서 찾고 클릭
#     element = driver.find_element(By.XPATH,
#                                     '//*[@id="mw-content-text"]/div/table[{}]/tbody/tr[{}]/td[2]/a'.format(6,
#                                                                                                              number + 2))
#     element.click()
#
#     # 개별 포켓몬 사이트호 이동함.
#     page_html = driver.page_source
#     soup = bs(page_html, 'html.parser')
#     try:  # 9세대 포켓몬들의 정보가 아직 추가되지 않음...
#         # 이름, 도감번호, 타입, 교배그룹, 키, 몸무게가 들어있는 테이블이다.
#         information_table = soup.findAll("table", style=re.compile(
#             r'float:right; text-align:center; width:33%; max-width:420px;.*?padding:2px;'))[0]
#         # 종족값이 들어있는 테이블
#         stats_table = soup.findAll("table", style=re.compile(
#             r'.*?border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; border:.*?white-space:nowrap'))[
#             0]
#         # 한글 이름이 들어있는 테이블
#         name_table = soup.findAll("table", {"class": "roundy"},
#                                     style=re.compile(r'background:.*?; border: 3px solid.*?; float:left'))[0]
#     except:
#         driver.back()
#         WebDriverWait(driver, timeout).until(element_present)
#         continue
#
#     # 포켓몬 정보를 추출해내는 과정:
#     # 포켓몬 이름
#     name = information_table.find("td", {"width": "75%", "class": "roundy", "style": "background:#FFF;"}).find(
#         "b").string
#     # 도감 번호
#     pokedex_number = int(
#         information_table.find("th", {"width": "25%", "class": "roundy", "style": "background:#FFF;"}).find(
#             "span").string[1:])
#     # 타입을 담을 리스트
#     pokemon_types = list()
#     # 타입을 추출해내는 과정
#     for table in information_table.findAll("td", {"class": "roundy"},
#                                            style=re.compile(r'background:.*?; padding:2px;')):
#         # Type이 들어있는 테이블인지 확인
#         if table.find("a").find("span").string == "Type":
#             # Display: None인 td들을 거르는 작업
#             type_td = table.findAll(lambda tag: tag.name == "td" and not tag.attrs)[0]
#             types = type_td.findAll("b")
#             # 단일 타입의 경우
#             if len(types) == 1:
#                 pokemon_types.append(types[0].string)
#                 pokemon_types.append("None")
#             # 타입이 세개 이상 적혀있는 경우가 있음. 이 점을 처리해야 함. (자시안처럼 따로 적혀있는 경우)
#             else:
#                 for t in types:
#                     pokemon_types.append(t.string)
#         # 메가진화 등으로 인해 타입이 두가지 방식으로 나타나는 경우
#         elif table.find("a").find("span").string == "Types":
#             # Display: None인 td들을 거르는 작업
#             type_td = table.findAll(lambda tag: tag.name == "td" and not tag.attrs)[0]
#             types = type_td.findAll("b")
#             # 단일 타입의 경우
#             if len(types) == 1:
#                 pokemon_types.append(types[0].string)
#                 pokemon_types.append("None")
#                 # 타입이 세개 이상 적혀있는 경우가 있음. 이 점을 처리해야 함. (자시안처럼 따로 적혀있는 경우)
#             else:
#                 for t in types:
#                     pokemon_types.append(t.string)
#
#     # 특성을 담을 리스트
#     abilities = list()
#
#     # 키 데이터를 담을 리스트
#     heights = list()
#
#     # 몸무게 데이터를 담을 리스트
#     weights = list()
#
#     tds = information_table.findAll("td", {"class": "roundy"})
#     for td in tds:
#         try:
#             # 특성 추출과정
#             if td.find("a").find("span").string == "Abilities":  # 특성이 여러개 있는 경우
#                 # display: none 이 있는 것들을 골라내야 함.
#                 ability_tds = td.findAll(lambda tag: tag.has_attr("width") and not tag.has_attr("style"))
#                 for ability_td in ability_tds:
#                     # 특성 추출
#                     ability = ability_td.findAll("span")
#                     for a in ability:
#                         abilities.append(a.string)
#             elif td.find("a").find("span").string == "Ability":  # 특성이 하나밖에 없는 경우
#                 # 첫 td를 골라냄
#                 abilities.append(td.find("td").find("span").string)
#
#         except:
#             pass
#
#         try:
#             # 키 데이터 추출과정
#             if td.find("a").find("span").string == "Height":
#                 height_tds = td.findAll("tr")[0].findAll("td")
#                 for height_td in height_tds:
#                     heights.append(height_td.string)
#
#             elif td.find("a").find("span").string == "Weight":
#                 weight_tds = td.findAll("tr")[0].findAll("td")
#                 for weight_td in weight_tds:
#                     weights.append(weight_td.string)
#         except:
#             pass
#
#     # 스텟을 담을 리스트. 순서대로 hp, attack, defense, sp_atk, sp_def, speed
#     stats = list()
#
#     stats_data = stats_table.findAll("tr", style=re.compile(r'background: #.*?; text-align:center'))
#     for data in stats_data:
#         stats.append(int(data.find("div", style="float:right").string))
#
#     # 데이터를 한곳에 모은다.
#     pokemon = dict()
#     pokemon["name"] = name
#     pokemon["pokedex_number"] = pokedex_number
#     pokemon["type1"] = pokemon_types[0]
#     pokemon["type2"] = pokemon_types[1]
#     pokemon["abilities"] = abilities
#     pokemon["hp"] = stats[0]
#     pokemon["atk"] = stats[1]
#     pokemon["def"] = stats[2]
#     pokemon["sp_atk"] = stats[3]
#     pokemon["sp_def"] = stats[4]
#     pokemon["speed"] = stats[5]
#     pokemon["height(in)"] = heights[0]
#     pokemon["height(m)"] = heights[1]
#     pokemon["weight(lbs)"] = weights[0]
#     pokemon["weight(kg)"] = weights[1]
#
#     pokemons.append(pokemon)
#
#     print(name)
#     print(pokedex_number)
#     print(pokemon_types)
#     print(abilities)
#     print(stats)
#     print(heights)
#     print(weights)
#     print("=================================================")
#
#     driver.back()
#     WebDriverWait(driver, timeout).until(element_present)
    # break
    # num += 1
    # break

# pokemon_df = pd.DataFrame(pokemons)
# pokemon_df.to_csv("Pokemon_Data_F.csv")

    for number in range(number_of_pokemons_by_alphabet):
        # 개별 포켓몬의 정보를 저장할 dictionary 만들기
        pokemon = dict()
        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="mw-content-text"]/div/table[{}]/tbody/tr[{}]/td[2]/a'.format(num + 1, number + 2)))
        # WebDriverWait(driver, timeout).until(element_present)
        # 목록에서 찾고 클릭
        element = driver.find_element(By.XPATH,
                                      '//*[@id="mw-content-text"]/div/table[{}]/tbody/tr[{}]/td[2]/a'.format(num + 1, number + 2))
        element.click()

        # 개별 포켓몬 사이트호 이동함.
        page_html = driver.page_source
        soup = bs(page_html, 'html.parser')
        try:  # 9세대 포켓몬들의 정보가 아직 추가되지 않음...
            # 이름, 도감번호, 타입, 교배그룹, 키, 몸무게가 들어있는 테이블이다.
            information_table = soup.findAll("table", style=re.compile(
                r'float:right; text-align:center; width:33%; max-width:420px;.*?padding:2px;'))[0]
            # 종족값이 들어있는 테이블
            stats_table = soup.findAll("table", style=re.compile(
                r'.*?border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; border:.*?white-space:nowrap'))[0]
            # 한글 이름이 들어있는 테이블
            name_table = soup.findAll("table", {"class": "roundy"},
                                      style=re.compile(r'background:.*?; border: 3px solid.*?; float:left'))[0]
        except:  # 추가되지 않은 포켓몬의 경우 뒤로가기를 누른 후 다음 포켓몬으로 건너뛴다.
            driver.back()
            WebDriverWait(driver, timeout).until(element_present)
            continue

        # 포켓몬 정보를 추출해내는 과정:
        # 포켓몬 이름
        name = information_table.find("td", {"width": "75%", "class": "roundy", "style": "background:#FFF;"}).find(
            "b").string
        # 도감 번호
        pokedex_number = int(
            information_table.find("th", {"width": "25%", "class": "roundy", "style": "background:#FFF;"}).find(
                "span").string[1:])
        # 타입을 담을 리스트
        pokemon_types = list()
        # 타입을 추출해내는 과정
        for table in information_table.findAll("td", {"class": "roundy"},
                                               style=re.compile(r'background:.*?; padding:2px;')):
            # Type이 들어있는 테이블인지 확인
            if table.find("a").find("span").string == "Type":
                # Display: None인 td들을 거르는 작업
                type_td = table.findAll(lambda tag: tag.name == "td" and not tag.attrs)[0]
                types = type_td.findAll("b")
                # 단일 타입의 경우
                if len(types) == 1:
                    pokemon_types.append(types[0].string)
                    pokemon_types.append("None")
                # 타입이 세개 이상 적혀있는 경우가 있음. 이 점을 처리해야 함. (자시안처럼 따로 적혀있는 경우)
                else:
                    for t in types:
                        pokemon_types.append(t.string)
            # 메가진화 등으로 인해 타입이 두가지 방식으로 나타나는 경우
            elif table.find("a").find("span").string == "Types":
                # Display: None인 td들을 거르는 작업
                type_td = table.findAll(lambda tag: tag.name == "td" and not tag.attrs)[0]
                types = type_td.findAll("b")
                # 단일 타입의 경우
                if len(types) == 1:
                    pokemon_types.append(types[0].string)
                    pokemon_types.append("None")
                    # 타입이 세개 이상 적혀있는 경우가 있음. 이 점을 처리해야 함. (자시안처럼 따로 적혀있는 경우)
                else:
                    for t in types:
                        pokemon_types.append(t.string)

        # 특성을 담을 리스트
        abilities = list()

        # 키 데이터를 담을 리스트
        heights = list()

        # 몸무게 데이터를 담을 리스트
        weights = list()

        tds = information_table.findAll("td", {"class": "roundy"})
        for td in tds:
            try:
                # 특성 추출과정
                if td.find("a").find("span").string == "Abilities":  # 특성이 여러개 있는 경우
                    # display: none 이 있는 것들을 골라내야 함.
                    ability_tds = td.findAll(lambda tag: tag.has_attr("width") and not tag.has_attr("style"))
                    for ability_td in ability_tds:
                        # 특성 추출
                        ability = ability_td.findAll("span")
                        for a in ability:
                            abilities.append(a.string)
                elif td.find("a").find("span").string == "Ability":  # 특성이 하나밖에 없는 경우
                    # 첫 td를 골라냄
                    abilities.append(td.find("td").find("span").string)

            except:
                pass

            try:
                # 키 데이터 추출과정
                if td.find("a").find("span").string == "Height":
                    height_tds = td.findAll("tr")[0].findAll("td")
                    for height_td in height_tds:
                        heights.append(height_td.string)

                elif td.find("a").find("span").string == "Weight":
                    weight_tds = td.findAll("tr")[0].findAll("td")
                    for weight_td in weight_tds:
                        weights.append(weight_td.string)
            except:
                pass

        # 스텟을 담을 리스트. 순서대로 hp, attack, defense, sp_atk, sp_def, speed
        stats = list()

        stats_data = stats_table.findAll("tr", style=re.compile(r'background: #.*?; text-align:center'))
        for data in stats_data:
            stats.append(int(data.find("div", style="float:right").string))

        # 데이터를 한곳에 모은다.
        pokemon = dict()
        pokemon["name"] = name
        pokemon["pokedex_number"] = pokedex_number
        pokemon["type1"] = pokemon_types[0]
        pokemon["type2"] = pokemon_types[1]
        pokemon["abilities"] = abilities
        pokemon["hp"] = stats[0]
        pokemon["atk"] = stats[1]
        pokemon["def"] = stats[2]
        pokemon["sp_atk"] = stats[3]
        pokemon["sp_def"] = stats[4]
        pokemon["speed"] = stats[5]
        pokemon["height(in)"] = heights[0]
        pokemon["height(m)"] = heights[1]
        pokemon["weight(lbs)"] = weights[0]
        pokemon["weight(kg)"] = weights[1]

        pokemons.append(pokemon)

        print(name)
        print(pokedex_number)
        print(pokemon_types)
        print(abilities)
        print(stats)
        print(heights)
        print(weights)
        print("=================================================")

        driver.back()
        WebDriverWait(driver, timeout).until(element_present)
        # break
    num += 1
    # break

    pokemon_df = pd.DataFrame(pokemons)
    pokemon_df.to_csv("Pokemon_Data.csv")

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
