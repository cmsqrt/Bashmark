# About Bashmark

Bashmark is an easy to use command line tool. It helps to bookmark shell commands and retrieve them later using fuzzy search.

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

After selecting the correct match, the result is copied to the pasteboard and can simply be pasted (e.g. CTRL+V, CMD+V).

# Managing Bashmark Commands

The current command list can be checked using the `bmark` command:

```
bmark --list
```

# Removing Bashmark

Deinstalling Bashmark is as easy as installing it. First, clean up the local data by running:

```
bmark --clean
```

Then uninstall using pip:

```
sudo -H pip uninstall Bashmark
```

That's it... All deinstalled and removed. If you'd like to save your Bashmark command history, prior to calling `bmark --clean`, simply copy the file  `~/.bashmark/command` to a folder of your choice.


