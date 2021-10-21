# Vroom - Rev Shell Generator

Vroom is an extensible command line reverse shell generator and listener inspired by [revshells](https://www.revshells.com/) and [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings).

## Use

<img alt="Vroom usage demo" width="600" src="./assets/vroom-demo.svg">

Vroom has two modes out of the box : `list` and `use` (see the Extend section below for information on adding new modes).

`vroom list` shows a list of all available shell types. `vroom list -t TYPE` shows a list of all templates available for a given shell type.

`vroom use TYPE IP` generates a default reverse shell to IP for the selected TYPE. `use` takes 4 optional arguments :
- `-t NUMBER` allows you to specify the template (default is 0, run `vroom list -t TYPE` for a list of available templates)
- `-p PORT` allows you to specify the target port (default is 4242)
- `-l` starts an nc listener for the shell
- `-o PATH` writes the shell to a file. 

## Install

Vroom is built for Python 3.8 and up using only the standard library - no external packages are required (but you'll need nc if you want to use the listening feature). To install Vroom, simply clone this repository.

## Extend

Vroom is extensible, meaning you can easily add your own shells and templates, and even additional operating modes.

**Shells and Templates**

Additional shells and templates can be added to Vroom by creating or modifying configuration files in `./registry/conf/`.

All configuration files should respect the "conf_*.py" naming convention and include a dictionary "conf" with keys "name" and "templates". Vroom will let you know if it finds any config files that don't meet these requirements, and it won't crash if you mess up your file. Once you've created the file, you're all set - Vroom will import your templates automatically and no additional configuration is required.

Here's an example of a valid "conf_boba.py" file for an imaginary language boba :

```python
conf = {
    "name": "boba",
    "templates": [
        "boba /bin/sh --> tcp-connect(%IP%, %PORT%)",
        "boba boba.threading(/bin/bash --> tcp-connect(%IP%, %PORT%), 4)",
    ]
}
```
**Modes and Arguments**

Vroom also dynamically loads its argument parsers at runtime, meaning that with a bit more programming nous you can extend Vroom's functionality to include entirely new modes.

This requires adding a '\*_conf.py' file to `parser.parser_configs`. A valid '*\_conf.py' file includes a  dictionary with keys "name" (the name of your new mode) and "arguments" (defining the mode's positional and optional arguments using Python's [argparse](https://docs.python.org/3/library/argparse.html) syntax).

You'll also want to define a handler function that your new mode can use to process command-line arguments. This handler function will be passed the mode's argument namespace and a VroomRegistry instance (providing access to all available shells and templates) - it's up to you to decide what it does with them! 