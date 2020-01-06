#!/usr/bin/env python3

import sys, gettext, getopt
from os import listdir
from os.path import isfile, join
from pprint import pprint

#locale.setlocale(locale.LC_ALL, '')
gettext.textdomain('passgen')
_ = gettext.gettext

dictionary_path = "./dictionaries/"

number_of_tokens = 7
available_token_types = {"numbers", "special_chars", "words"}
token_types_to_use = available_token_types
short_options = "hnNsSwWi:e:"
long_options = ("help",
	"exclude-langs=",
	"help",
	"include-langs=",
	"no-numbers",
	"no-special",
	"no-words",
	"numbers",
	"special",
	"words",
)

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

languages = sorted(languages, key=lambda k: k['name'])


def get_all_available_languages():
	all_languages = []
	for lang in languages:
		all_languages.append(lang["code"])
	return all_languages


usable_languages = get_all_available_languages()


def include_languages(langs):
	global usable_languages
	langs = langs.split(',')
	usable_languages = []
	all_languages = set(get_all_available_languages())
	for lang in langs:
		lang = lang.lower()
		if lang in all_languages:
			usable_languages.append(lang)


def exclude_languages(langs):
	global usable_languages
	langs = langs.split(',')
	usable_languages = get_all_available_languages()
	for lang in langs:
		lang = lang.lower()
		if lang in usable_languages:
			usable_languages.remove(lang)


def help():
	available_languages = '\t\tLanguage\tCode\n\n'
	for language in languages:
		spaces = ' '* (8 - len(language['name']))
		available_languages += '''\t\t{0}{1}\t{2}\n'''.format(
			language['name'],
			spaces,
			language['code']
		)
	help_message = '''
Usage:

	{0} [-e|--exclude-langs=LANG_LIST] [-i|--include-langs=LANG_LIST] [-h] [-n|-N] [-s|-S] [-w|-W]

		-e --exclude-langs LANG_LIST   exclude the languages listed in LANG_LIST when creating word tokens. All languages not present in this option will be used. LANG_LIST should be a comma separated list of language two letter codes. See LANGUAGES CODES below. If both -e and -i options are present, only the last one is effective.
		-h --help                      show this help message
		-i --include-langs LANG_LIST   include the languages listed in LANG_LIST when creating word tokens. Only the languages present in this option will be used. LANG_LIST should be a comma separated list of language two letter codes. See LANGUAGES CODES below. If both -e and -i options are present, only the last one is effective.
		-n --numbers                   include number tokens in generated password (DEFAULT)
		-N --no-numbers                don't include number tokens in generated password
		-s --special-chars             include special character tokens in generated password (DEFAULT)
		-S --no-special-chars          don't include special character tokens in generated password
		-w --words                     include word tokens in generated password (DEFAULT)
		-W --no-words                  don't include word tokens in generated password


		LANGUAGE CODES

		Codes for the languages available at passgen:

{1}

	'''.format(sys.argv[0], available_languages)
	print(help_message)


def main(argv):
	try:
		opts, args = getopt.getopt(argv, short_options, long_options)
	except getopt.GetoptError:
		help()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-e', '--exclude-langs'):
			exclude_languages(arg)
		elif opt in ("-h", "--help"):
			help()
			sys.exit()
		elif opt in ("-i", "--include-langs"):
			include_languages(arg)
		elif opt in ("-n", "--numbers"):
			if "numbers" not in token_types_to_use:
				token_types_to_use.add("numbers")
		elif opt in ("-N", "--no-numbers"):
			if "numbers" in token_types_to_use:
				token_types_to_use.remove("numbers")
		elif opt in ("-s", "--special-chars"):
			if "special" not in token_types_to_use:
				token_types_to_use.add("special")
		elif opt in ("-S", "--no-special-chars"):
			if "special" in token_types_to_use:
				token_types_to_use.remove("special")
		elif opt in ("-w", "--words"):
			if "words" not in token_types_to_use:
				token_types_to_use.add("words")
		elif opt in ("-W", "--no-words"):
			if "words" in token_types_to_use:
				token_types_to_use.remove("words")
	pprint(usable_languages)
	pprint(token_types_to_use)

if __name__ == "__main__":
	main(sys.argv[1:])


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
