# -*- coding:utf8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError

def getTitle(url):

	try:
		html = urlopen(url)
		
	except (HTTPError,URLError) as e:
		return None

	try:
		bs_obj = BeautifulSoup(html.read())
		title = bs_obj.title
	except AttributeError as e:
		return None

	return title

title = getTitle("https://bing.com")
if title == None:
	print('none')
else:
	print(title)
