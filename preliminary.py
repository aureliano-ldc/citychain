
""" 数据预处理 """

import requests

from bs4 import BeautifulSoup

# 爬取并处理城市数据
city_url = 'http://data.acmr.com.cn/member/city/city_md.asp#'

def get_cities():
	headers = {'User-Agent':
		   	   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}

	data = requests.get(city_url, headers=headers).content
	soup = BeautifulSoup(data, 'html.parser')
	cats = soup.find_all('table', "maintext", width="500")

	cities = []
	for cat in cats[5:34]:
		cities.extend(list(cat.stripped_strings))

	try:
		while cities.index('[TOP]'):
			del(cities[cities.index('[TOP]')])  
	except ValueError:
		print('done')

	for city in cities:
		try:
			if len(city) == city.index('省') + 1:
				del(cities[cities.index(city)])
		except ValueError:
			continue

	for city in cities:
		try:
			a = city.index('省') + 1
			b = city.index('市')
			ix = cities.index(city)
			city = city[a:b]
			cities[ix] = city
		except ValueError:
			continue		

	for city in cities:
		if city[-1] == '市':
			ix = cities.index(city)
			city = city[:-1]
			cities[ix] = city	

	for city in cities:
		if city[0:2] == '新疆' and len(city) > 2:
			ix = cities.index(city)
			city = city[2:]		
			cities[ix] = city	
		elif city[0:2] == '广西' and len(city) > 2:
			ix = cities.index(city)
			city = city[2:]		
			cities[ix] = city
		elif city[0:2] == '宁夏' and len(city) > 2:
			ix = cities.index(city)
			city = city[2:]		
			cities[ix] = city	
		elif city[0:3] == '重庆市' and len(city) > 3:		
			ix = cities.index(city)
			city = city[3:]		
			cities[ix] = city	
		elif city[0:2] == '内蒙' and len(city) > 2:
			ix = cities.index(city)
			city = city[2:]		
			cities[ix] = city	



	cities = set(cities)
	cities.remove('地级及以上城市:')
	cities.remove('县级市:')
	cities = list(cities)

	return cities


""" 为每个城市加上拼音:
	imput: a list of cities in Chinese
	output: a dict of cities, 
			in which keys represent cities in Chinese and values represent pinyin
"""
from xpinyin import Pinyin

p = Pinyin()

def get_cities_with_pinyin(list_cities):
	dict_cities = {}
	for city in list_cities:
		p_city = p.get_pinyin(city)
		p_city = p_city.split('-')
		dict_cities[city] = p_city
	return dict_cities
