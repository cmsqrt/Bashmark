import pyperclip
import pickle
import os
import sys
import shutil
import time
from fuzzywuzzy import process

# paths for different files
PATH_HOME_DIR = os.path.expanduser("~")
PATH_BASE_DIR = '%s/.bashmark' % PATH_HOME_DIR
PATH_COMMAND_STORE = '%s/commands' % PATH_BASE_DIR
PATH_LAST_COMMAND = '%s/last' % PATH_BASE_DIR
PATH_PROMPT_EXTENSION = '%s/prompt_extension' % PATH_BASE_DIR
PATH_BASH_PROFILE = '%s/.bash_profile' % PATH_HOME_DIR
PATH_BASH_PROFILE_TEMP = '%s/.bash_profile_tmp' % PATH_HOME_DIR


# constants
CO_BASH_PROFILE_ADDITION_COMMENT = "# Added by bashmark remove with 'bmark --clean'"
CO_BASH_PROFILE_ADDITION = "if [ -f ~/.bashmark/prompt_extension ]; then source ~/.bashmark/prompt_extension; fi"
CO_PROMPT_EXTENSION = "[[ ! -d \"~/.bashmark\" ]]||history 1 | sed 's/^ *[^ ]* *//' | cut -d$'\\n' -f1 > ~/.bashmark/last"

def check_init():
	"""
	 check if bashmark init was done
	:return: True if yes, False if not
	"""

	# check basedire
	return os.path.exists(PATH_BASE_DIR)



def read_last_bash_command():

	last_command_file = open(PATH_LAST_COMMAND, 'rb')
	command = last_command_file.read()

	# return without new line
	return command[:-1]


def get_commands_dict():
	try:
		commands_file = open(PATH_COMMAND_STORE, 'rb')
	except:
		new_dict = dict()
		new_dict['commands'] = list()
		new_dict['descriptions'] = list()

		return new_dict

	command_dict = pickle.load(commands_file)
	return command_dict


def perform_search(query):

	command_dict = get_commands_dict()
	fuzzy_matches = process.extract(query, command_dict['descriptions'])

	index = 1
	print "\nBest Matches\n"
	for match in fuzzy_matches[:10]:
		print '%i: %s (%u%%)' %(index, match[0], match[1])
		index += 1

	a = raw_input('\n(Exit with 0): ')
	print

	selected = fuzzy_matches[int(a)-1][0]
	selected_index = command_dict['descriptions'].index(selected)
	selected_command = command_dict['commands'][selected_index]

	if selected_command:
		pyperclip.copy(selected_command)


def perform_search_force(query):

	command_dict = get_commands_dict()
	fuzzy_match = process.extractOne(query, command_dict['descriptions'])
	selected_index = command_dict['descriptions'].index(fuzzy_match[0])
	selected_command = command_dict['commands'][selected_index]

	if selected_command:
		pyperclip.copy(selected_command)


def bashmark_clean():
	"""
		Remove base dir and bash profile reference
	:return:
	"""

	# clean bash profile...
	with open(PATH_BASH_PROFILE, "r") as input:
		with open(PATH_BASH_PROFILE_TEMP, "wb") as output:
			for line in input:
				if CO_BASH_PROFILE_ADDITION not in line and CO_BASH_PROFILE_ADDITION_COMMENT not in line:
					output.write(line)

	os.rename(PATH_BASH_PROFILE, PATH_BASH_PROFILE + ".%s" % time.strftime("%Y%m%d%H%M%S"))
	os.rename(PATH_BASH_PROFILE_TEMP, PATH_BASH_PROFILE)

	# remove base directory
	if os.path.exists(PATH_BASE_DIR):
		shutil.rmtree(PATH_BASE_DIR)


def bashmark_init():
	"""
		init bashmark

		 1 - generate prompt command extension
		 2 - add it to bash profile
	 	 3 - reset commands list

	"""

	# create base path
	if not os.path.exists(PATH_BASE_DIR):
		os.mkdir(PATH_BASE_DIR)

	# write path extension script
	file = open(PATH_PROMPT_EXTENSION, 'w')
	file.write(
		"PROMPT_COMMAND=\"$PROMPT_COMMAND;%s\"" % CO_PROMPT_EXTENSION)
	file.write("\nexport PROMPT_COMMAND\n")
	file.close()

	# add script to bash profile
	file = open(PATH_BASH_PROFILE, 'a')
	file.write('\n')
	file.write(CO_BASH_PROFILE_ADDITION_COMMENT)
	file.write('\n')
	file.write(CO_BASH_PROFILE_ADDITION)
	file.write('\n\n')
	file.close()

	# move existing store
	if os.path.exists(PATH_COMMAND_STORE):
		os.rename(PATH_COMMAND_STORE, PATH_COMMAND_STORE + ".%s" % time.strftime("%Y%m%d%H%M%S") )

	# info to user...
	print("\nSuccessfully initialized Bashmark.\n")
	print("Please run 'source ~/.bash_profile' or restart the shell to enable history tracking.\n")

def bashmark_list():

	command_dict = get_commands_dict();
	print
	for a in range(0, len(command_dict['commands'])):
		print("%i: %s - \"%s\"" % (a + 1, command_dict['descriptions'][a], command_dict['commands'][a]))
	print


def add_new(description, a_command):

	command = ''
	if a_command == '' or a_command == None:
		command = read_last_bash_command()
	else:
		command = a_command

	command_dict = get_commands_dict()

	command_dict['commands'].append(command)
	command_dict['descriptions'].append(description)

	with open(PATH_COMMAND_STORE, 'wb') as fp:
		pickle.dump(command_dict, fp)
