# About Bashmark

Ever forgot this one command? How did I do this rename in bash? What was the option to grep with... right! That's what Bashmark is for!

It is an easy to use command line tool and will help you to bookmark shell commands and retrieve them later using fuzzy search.

# Installing Bashmark

If you have `pip` installed on your machine, installing Bashmark is super-easy. Simply run:

```
sudo -H pip install git+https://github.com/cmsqrt/Bashmark.git
bmark --init
``` 

After the init completes, either restart your shell or run `source ~/.bash_profile`.

# Using Bashmark

Adding the latest command to Bashmark is easy - there are 3 core operations `++`, to add a command to bashmark, `??`, to query for any command added earlier and `??!` to retrieve the best match without additional user interaction.

To add the last command, simply:

```
++ "<Description of the command>"
```

If you'd like to store a different command, simply use the `--command` option:

```
++ "<Description of the command>" --command="<Actual command>"
```

To query for anything, just use `??`, this will basically perform a fuzzy search in the commands db:

```
?? "Query text"
```

After selecting the correct match, the result is copied to the pasteboard and can simply be pasted e.g. with **CTRL+V**, or  **CMD+V**.

# Example

Check out this simple example:

```
cmsqrt@home$ sed -i -e 's/abc/XYZ/g' /tmp/file.txt
cmsqrt@home$ ++ "replace string in text file"
cmsqrt@home$ bmark --list

1: get ssh public key - "pbcopy < ~/.ssh/id_rsa.pub"
2: generate new ssh key - "ssh-keygen -t rsa"
3: mass rename of files - "for i in x*; do mv x* x*.jp.strings; done"
4: bashmark git clone - "git clone git@github.com:cmsqrt/Bashmark.git"
5: split files complete lines - "split -l 140 en_orig.strings"
6: change shell prompt to cmsqrt - "export PS1="cmsqrt@home$ ""
7: default shell prompt - "export PS1="\h:\W \u\$ ""
8: cw current calendar week - "date +"%V""
9: zeige mir was - "ps -eax"
10: install bashmark - "sudo -H pip install git+https://github.com/cmsqrt/Bashmark.git"
11: list all commands bashmark - "bmark --list"
12: replace string in text file - "sed -i -e 's/abc/XYZ/g' /tmp/file.txt"

cmsqrt@home$ ?? replace

Best Matches

1: replace string in text file (90%)
2: mass rename of files (51%)
3: get ssh public key (40%)
4: generate new ssh key (39%)
5: split files complete lines (39%)

(Exit with 0): 1

cmsqrt@home$ sed -i -e 's/abc/XYZ/g' /tmp/file.txt
cmsqrt@home$ ??! replace
cmsqrt@home$ sed -i -e 's/abc/XYZ/g' /tmp/file.txt
```

# Managing Bashmark Commands

The current command list can be checked using the `bmark` command:

```
bmark --list
```
This command will output an indexed list of all commands. To remove a specific command, simply run

```
bmark --remove 4
```

This would remove command 4 from the list of commands.

# Removing Bashmark

Deinstalling Bashmark is as easy as installing it. First, clean up the local data by running:

```
bmark --clean
```

Then uninstall using pip:

```
sudo -H pip uninstall Bashmark
```

That's it... All deinstalled and removed. If you'd like to save your Bashmark command history, prior to calling `bmark --clean`, simply copy the file  `~/.bashmark/commands.json` to a folder of your choice.


