#!/bin/env python3

import click
import pathlib
import glob
from termcolor import colored

scripts_file = pathlib.Path(__file__).resolve().parent / "source" / ".source_files"
scripts_file.touch()

scripts = {}

buf = scripts_file.open()
for script in buf:
    name, file = script.strip(" \n").split(" ")
    scripts[name] = file
buf.close()

def write_scripts():
    buf = scripts_file.open("w")
    for name, file in scripts.items():
        buf.write(f"{name} {file}\n")
    buf.close()


command = click.Group("source")

command.help = "Control Source Scripts"

@command.command("list")
def list():
    """List Currently Sourced Scripts"""
    print()
    for name, file in scripts.items():
        print(f"{name} - {file}")
    print()


def add_autocomplete(ctx, param, incomplete):
    arr = glob.glob(f"{incomplete}*")
    if len(arr) == 1 and '.' not in arr:
       return add_autocomplete(ctx, param, arr[0] + "/")
    return arr

@command.command("add")
@click.argument("name")
@click.argument("file", shell_complete=add_autocomplete)
def add(name, file):
    """Add a New Script to be Sourced"""

    path = pathlib.Path(file)

    if not path.is_file():
        print(f"{colored('Error', 'red')} - File not Found")

    scripts[name] = str(path.absolute().resolve())

    write_scripts()

    print(f"Added {file} to Sourced Scripts")


def rm_autocomplete(ctx, param, incomplete):
    return [i for i in scripts.keys() if i.startswith(incomplete)]

@command.command("rm")
@click.argument("name", shell_complete=rm_autocomplete)
def rm(name):
    """Stop a Script from Being Sourced"""
    if name in scripts.keys():
        scripts.pop(name)
        write_scripts()
        print(f"Removed {name}")
    else:
        print(f"{colored('Error')} - Script is not Sourced Currently")
