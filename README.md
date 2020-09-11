
# cmd-Vocab-Quotes
This repository contains two Python Scripts that do the following -
* wod.py - The script parses through 2 json files that contain famous motivational quotes (quotes.json) and word with it's meaning and it's grammar. Hence displaying the same on the command line.
* wotd.py - The script scrapes off **Word Of The Day**  from www.dictionary.com and displays it on the the command line along with its meaning and pronounciation.

This script is to be implemented on a Text Editor.

## Getting Started

### Packages
1. wod.py
	* json - To parse through the json files.
	* random- To randomize the display in.
2. wotd.py
	* BeautifulSoup - To use as HTML parser.
	* requests - To obtain the URL and page.
	* string - To manipulate the strings obtained.

### To add it to the CMD
```
$ cd ../..
$ cd etc
$ texteditor bash.basrc
```
On line 1 add the following & save it-
```
python3 /address of the script/wotd.py[or]wod.py
```

## Built with
* Python
## Author
* **Nikita Kodkany** - *Student*
