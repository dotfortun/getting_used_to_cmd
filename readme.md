# Command Line Tools

This codebase has everything that you need for a fully functioning Flask app.

To get it running, however, you will be asked to interact with this via the command line.

### Getting started:
1) Start this as a Gitpod project [by clicking here](https://gitpod.io/#https://github.com/dotfortun/getting_used_to_cmd).
2) Hit ``` ctrl+` ``` to open the terminal.

### Useful shortcuts:
* ```ctrl+c``` ends a running process in the terminal.
* ```ctrl+v``` pastes your clipboard to the terminal.  The first time you do this in Gitpod, there will be a popup asking for permission.
* ```TAB``` autocompletes for you in the terminal.

### The structure of a command line command:

Most things on the command line will be formatted like this (give or take): ```command -args "input.txt" "output.txt"```

To break this down, ```command``` is the name of the program you are running.

Everything after the main command is either a subcommand or an argument.  Subcommands are, for all intents and purposes, just arguments without dashes.

```-args``` is actually 4 arguments, ```-a```, ```-r```, ```-g```, and ```-s``` but they are grouped behind one dash.  Most but not all arguments have both a short and a long version.

An argument tells the computer more information about what you want to do.  For example, try ```ls``` and then ```ls -alh```, and see the difference for yourself.

For the command ```ls -alh``` you have 3 arguments that are passed to the program:
* ```-a``` - This tells ls to show ```--all``` the files, including files that are hidden.
* ```-l``` - This tells ls to show the output in ```--list``` format.
* ```-h``` - This tells ls to show the size of the the files in ```--human-readable``` units.

#### Website template: https://github.com/luisbraganca/fake-terminal-website
