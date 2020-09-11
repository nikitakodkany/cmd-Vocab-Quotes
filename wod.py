#Displays random word from the dictionary(json file)

import json
import random as r

cyan = '\033[36;1m'
yellow = '\033[33;1m'
white_faint = '\033[37;2m'
white_italics = '\033[37;3m'
ENDC = '\033[m'

with open('/home/nikita/Documents/wotd/quotes.json') as q:
    qdata = json.load(q)

qn = r.randint(1,len(qdata))
quote = qdata[qn]

print()
print(white_italics, quote['text'], ENDC)
print("                   -",yellow, quote['from'], ENDC)

with open('/home/nikita/Documents/wotd/dictionary.json') as f:
    data = json.load(f)

n = r.randint(1,len(data))
wod = data[n]
meaning = wod['definitions']

print()
print(cyan, wod['word'], ENDC, ":", white_faint, wod['pos'],ENDC)
print(meaning[0])
print()
