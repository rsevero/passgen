#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join

dictionary_path = "./dictionaries/"

def get_file_line_count(fname):
	i = -1
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

# Reading dictionaries.

for filename in listdir(dictionary_path):
	fullpath = join(dictionary_path, filename)
	if not(isfile(fullpath)):
		break
	line_count = get_file_line_count(fullpath)
	print("File:", filename, "- Line count:", line_count)
