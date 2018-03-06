import os
import sys
import argparse
from Bashmark import implementation

# internal command mapping
CO_OPERATION_ADD = 'add'  # all ++ operations
CO_OPERATION_SEARCH = 'search'  # all ?? operations
CO_OPERATION_SEARCH_F = 'searchforce'  # all ??! operations
CO_OPERATION_MANAGE = 'manage'  # all bmark operations

# helper functions
def arguments_for(operation):

	parser = None

	if operation == CO_OPERATION_ADD:
		parser = argparse.ArgumentParser(description='Add shell commands to bookmark repository.')
		parser.add_argument('description', type=str, help='Searchable description')
		parser.add_argument('--command', type=str, help='Actual command')

	elif operation == CO_OPERATION_SEARCH:
		parser = argparse.ArgumentParser(description='Search for commands.')
		parser.add_argument('query', type=str, help='Search query')

	elif operation == CO_OPERATION_SEARCH_F:
		parser = argparse.ArgumentParser(description='Search for commands, copy best rated to clipboard.')
		parser.add_argument('query', type=str, help='Search query')

	elif operation == CO_OPERATION_MANAGE:
		parser = argparse.ArgumentParser(description='Manage Bashmark.')
		parser.add_argument('--init', action='store_true', help='Initialize bashmark')
		parser.add_argument('--clean', action='store_true', help='Remove bashmark data')
		parser.add_argument('--list', action='store_true', help='List all bookmarked commands')
		parser.add_argument('--remove', metavar="INDEX", type=int, help='Remove command at index')

	args = parser.parse_args()
	return args


def check():
	if not implementation.check_init():
		print("Bashmark is not initialized. Run 'bmark --init'.")
		exit(1)

# all operations

def add_new():
	check()
	args = arguments_for(CO_OPERATION_ADD)
	implementation.add_new(args.description, args.command)


def search():
	check()
	args = arguments_for(CO_OPERATION_SEARCH)
	implementation.perform_search(args.query)


def search_force():
	check()
	args = arguments_for(CO_OPERATION_SEARCH)
	implementation.perform_search_force(args.query)


def bashmark():
	args = arguments_for(CO_OPERATION_MANAGE)
	if args.init:
		implementation.bashmark_init()
	elif args.list:
		implementation.bashmark_list()
	elif args.clean:
		implementation.bashmark_clean()
	elif args.remove:
		implementation.bashmark_remove(args.remove)