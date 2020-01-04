#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import gettext
from pprint import pprint

#locale.setlocale(locale.LC_ALL, '')
gettext.textdomain('passgen')
_ = gettext.gettext

dictionary_path = "./dictionaries/"

languages = [
	{
		"code": "fr",
		"file": "francais.txt",
		"name": _("french"),
	},
	{
		"code": "en",
		"file": "english.txt",
		"name": _("english"),
	},
	{
		"code": "es",
		"file": "espanoal.txt",
		"name": _("spanish"),
	},
	{
		"code" : "pt",
		"file": "portugues.txt",
		"name": _("portuguese"),
	},
]

available_languages = sorted(languages, key=lambda k: k['name'])
pprint(available_languages)

# def get_file_line_count(fname):
# 	i = -1
# 	with open(fname) as f:
# 		for i, l in enumerate(f):
# 			pass
# 	return i + 1

# # Reading dictionaries.

# for filename in listdir(dictionary_path):
# 	fullpath = join(dictionary_path, filename)
# 	if not(isfile(fullpath)):
# 		break
# 	line_count = get_file_line_count(fullpath)
# 	print("File:", filename, "- Line count:", line_count)
