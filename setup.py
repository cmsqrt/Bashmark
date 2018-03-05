from setuptools import setup
setup(
		name='Bashmark',
	  	version='0.4.2',
		install_requires = ['pyperclip', 'fuzzywuzzy', 'python-Levenshtein'],
	  	entry_points =
	  	{
              'console_scripts': [
                  '++ = Bashmark.bashmark:add_new',
                  '?? = Bashmark.bashmark:search',
				  '??! = Bashmark.bashmark:search_force',
				  'bmark = Bashmark.bashmark:bashmark']
	  	})

# pip command
#  sudo -H pip install -e bmt/
#  sudo -H pip uninstall BashBook
# bmark --init
# $PROMPT_COMMAND
# update_terminal_cwd;history 1 | sed 's/^ *[^ ]* *//' | cut -d$'\n' -f1 > ~/.bashmark_last
# .bashrc
#  PROMPT_COMMAND=$PROMPT_COMMAND;history 1 | sed 's/^ *[^ ]* *//' | cut -d$'\n' -f1 > ~/.bashmark_last
# export PROMPT_COMMAND
#pip install git+https://github.com/tangentlabs/django-oscar-paypal.git