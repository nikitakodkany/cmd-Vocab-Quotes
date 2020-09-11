#Word of the Day from www.dictionary.com (web scrapping)

from bs4 import BeautifulSoup
import requests as rq
import string

url = "https://www.dictionary.com/e/word-of-the-day/"
page = rq.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

wotd_word = soup.find('div', class_='wotd-item-headword__word')
wotd_pronunciation = soup.find('div', class_='wotd-item-headword__pronunciation')
wotd_meaning = soup.find('div', class_='wotd-item-headword__pos')

cyan = '\033[36;1m'
white_italics = '\033[37;3m'
white_faint = '\033[37;2m'
ENDC = '\033[m'

wotd_m = wotd_meaning.text.strip()
word_msl = str.split(wotd_m, '\n')

print()
print(cyan, wotd_word.text.strip() ,ENDC, white_italics, wotd_pronunciation.text.strip(), ENDC, ":", white_faint, word_msl[0], ENDC)
print(word_msl[2])
print()
