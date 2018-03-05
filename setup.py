from setuptools import setup
setup(
		name='Bashmark',
	  	version='0.4.2',
		py_modules=['Bashmark'],
		install_requires = ['pyperclip', 'fuzzywuzzy', 'python-Levenshtein'],
	  	entry_points =
	  	{
              'console_scripts': [
                  '++ = Bashmark.bashmark:add_new',
                  '?? = Bashmark.bashmark:search',
				  '??! = Bashmark.bashmark:search_force',
				  'bmark = Bashmark.bashmark:bashmark']
	  	})
