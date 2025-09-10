#!/bin/env python3

import importlib
import click
import os, sys
import types

# Subcommand list with name as key and short help info as value
subcommands = {
    "env": "Controls environment sourced on shell creation"
}

sys.path.append(os.path.join(os.path.dirname(__file__), "subcommands"))

# Create the subcommand group
@click.group("uwrt")
def uwrt():
    pass


# For all pairs in subcommands create a command callback that loads
# and invokes the subcommand at runtime
for k,v in subcommands.items():
        mod = importlib.import_module(k)
        command: click.Command = getattr(mod, "command")
        uwrt.add_command(command)

if __name__ == "__main__":
    uwrt()
