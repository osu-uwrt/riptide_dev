import click
import pathlib
from termcolor import colored


command = click.Group("alias")

command.help = "Configure Bash Aliases"

bash_file = pathlib.Path(__file__).resolve().parent / "source" / "alias.bash"

aliases = {}

script = bash_file.open("r")

# Bypass first 2 lines
script.readline()
script.readline()

for line in script:
    alias = line[len("alias "):].split("=")
    aliases[alias[0]] = alias[1]

script.close()

def write_aliases():
    script = bash_file.open("w")

    script.write("#!/bin/bash\n\n")

    for alias, cmd in aliases.items():
        script.write(f"alias {alias}='{cmd}'\n")

    script.close()

@command.command("list")
def list():
    """List Current Bash Aliases"""
    
    for alias, cmd in aliases.items():
        # Newline is already there
        print(f"{alias} -> {cmd}", end="")

@command.command("set")
@click.argument("alias")
@click.argument("command")
def set(alias, command):
    """
    Create a New Alias

    Create a new alias named ALIAS that runs COMMAND
    If using an environment variable in the alias use single quotes to prevent expansion.
    """

    aliases[alias] = command

    write_aliases()

    print("Re-source .bashrc to use new alias")


def delete_help(ctx, param, incomplete):
    return [i for i in aliases.keys() if i.startswith(incomplete)]

@command.command("delete")
@click.argument("alias")
def delete(alias):
    """Delete an Alias"""

    aliases.pop(alias)

    write_aliases()

    print(f"Removed {alias}")
    print("Terminal must be reset for changes to take effect")
