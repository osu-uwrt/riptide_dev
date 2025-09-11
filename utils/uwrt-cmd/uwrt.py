#!/bin/env python3

from pathlib import Path
import importlib
import click
import os, sys
import types


wd = Path(__file__).resolve().parent
modules = wd.glob("*.py")


# Create the subcommand group
@click.group("uwrt")
def uwrt():
    pass


# For all pairs in subcommands create a command callback that loads
# and invokes the subcommand at runtime
for mod_file in modules:
    if mod_file.name == "uwrt.py":
        continue

    mod = importlib.import_module(mod_file.name.split('.')[0])
    command: click.Command = getattr(mod, "command")
    uwrt.add_command(command)

if __name__ == "__main__":
    uwrt()
