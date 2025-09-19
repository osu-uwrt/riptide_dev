#!/bin/env python3

import click
import os
import yaml
import pathlib
from termcolor import colored

# Parse Config File
config_file = pathlib.Path(__file__).parent / "config" / "rmw.yaml"
config: dict = yaml.safe_load(config_file.open())

# Writes config back to file
def write_config():
    yaml.dump(config, config_file.open("w"))

bash_file = pathlib.Path(__file__).parent / "source" / "rmw.yaml"

def write_bash():
    bash_script = bash_file.open("w")

    bash_script.write("#!/bin/bash\n\n")
    
    rmw = config["active"]
    bash_script.write(f"export RMW_IMPLEMENTATION={rmw}\n")

    for opt, data in config["middleware"][rmw]["options"].items():
        bash_script.write(f"export {opt}={data['value']}\n")

    bash_script.close()

# Create Command Group
command = click.Group("rmw")

command.short_help = "Configure ROS Middleware"

@command.command("list")
def list():
    """
    List the available middlewares

    Active Middleware (Green)
    """
    for key in config["middleware"].keys():
        desc = config["middleware"][key]["description"]

        if "active" in config.keys() and key == config["active"]:
            print(f"{colored(key, 'green')} - {desc}")
        else:
            print(f"{colored(key, 'red')} - {desc}")


def complete_set(ctx, param, incomplete):
    return [ i for i in config["middleware"].keys() if i.startswith(incomplete) ]

@command.command("use")
@click.argument("middleware", shell_complete=complete_set)
def use(middleware: str):
    """
    Set the Active Middleware
    """

    if middleware in config["middleware"].keys():
        config["active"] = middleware
        write_config()
        write_bash()
        print(f"Using {middleware}")
        print(".bashrc must be re-sourced to update RMW")
    else:
        print(f"{middleware} is not a configurable middleware")
        print("To add middleware to this plugin check the configuration file.")
        print(str(config_file))


def option_autocomplete(ctx, param, incomplete):
    if "active" not in config.keys() and config["active"] not in config["middleware"].keys():
        print("Invalid Middleware Active")
        exit(1)
    
    return [i for i in config["middleware"][config["active"]]["options"].keys() if i.startswith(incomplete)]

@command.command("options")
@click.argument("name", required=False, shell_complete=option_autocomplete)
@click.argument("value", required=False)
def options(name, value):
    """
    Sets Options for the Active Middleware

    If NAME and VALUE are set then the option with the given name
    will be set to the given value.

    If NAME and VALUE are unset then all the options are output with
    their value and a description of what the option does.

    If just the NAME is specified the option and it's value are output.
    """

    # Check if active middleware is valid
    if "active" not in config.keys() and config["active"] not in config["middleware"].keys():
        print("Invalid Middleware Active")
        exit(1)
    
    middleware = config["active"]
    options: dict[str, Any] = config["middleware"][middleware]["options"]

    # If option-name is specified it must be valid
    if name is not None and name not in options.keys():
        print(f"{name} option doesn't exist")

    if name is None:
        for k, v in options.items():
            desc = v["description"] if "description" in v.keys() else "No Description"
            value = v["value"] if "value" in v.keys() else ""
            print(f"{k}={value}")
            print(desc)
            print()
    elif value is not None:
        options[name]["value"] = value
        write_config()
        write_bash()
        print(f"{name}={value}")
    else:
        print(f"{name}={options[name]['value']}")
