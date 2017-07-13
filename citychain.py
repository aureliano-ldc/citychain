
"""城语接龙 """

from preliminary import *

from xpinyin import Pinyin

from random import randint

p = Pinyin()

cities = get_cities()

data = get_cities_with_pinyin(cities)

def cityChain(my_city):
	potentials = {}	
	p_my_city = p.get_pinyin(my_city)
	p_my_city = p_my_city.split('-')
	for city, pinyin in data.items():
		if pinyin[0] == p_my_city[-1]:
			potentials[city] = pinyin
	if len(potentials) == 0:
		return 0
	else:
		ix = randint(0, len(potentials)-1)
		return list(potentials.keys())[ix]


def main():
	input_city = input("请输入城市：") 
	result = cityChain(input_city)
	if result == 0:
		print("接不下去了，OVER")
	while result != 0:
		print(result)
		answer = input("是否继续？(Y/N): ")
		result = cityChain(result)		
	print("接龙结束，OVER")

