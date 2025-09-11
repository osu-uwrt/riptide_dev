import click
import os
from pathlib import Path
from termcolor import colored

uwrt_path = os.getenv("UWRT_PATH")
if uwrt_path is None:
    print(colored("UWRT Path not Set", "red"))

sources_path = Path(uwrt_path) / "utils" / "scripts" / "source"

# Returns list of all enabled scripts
def enabled(ctx, param, incomplete):
    comp: list[str] = []
    for file in sources_path.glob("*.bash"):
        if file.name.startswith(incomplete):
            comp.append(file.name)

    return comp

# Returns list of all disabled scripts
def disabled(ctx, param, incomplete):
    comp: list[str] = []
    for file in sources_path.glob("*.bash.d"):
        if file.name.startswith(incomplete):
            comp.append(file.name[0:-2])

    return comp


@click.group("source")
def command():
    pass

help = f"List {colored('Enabled', 'green')} and {colored('Disabled', 'red')} sources"
@command.command("list", help=help)
def list():
    """List Active(Green) and Inactive(Red) Sources"""
    files = sources_path.glob("*")

    for file in files:
        if file.name.endswith(".bash"):
            print(colored(file.name, "green"))
        elif file.name.endswith(".bash.d"):
            print(colored(file.name[0:-2], "red"))



@command.command("enable")
@click.argument("script", shell_complete=disabled)
def enable(script):
    """Enable a Source Script"""

    enabled_path = sources_path / script
    disabled_path = sources_path / (script + ".d")

    # Check if script is already enabled
    if enabled_path.is_file():
        print("Script is already enabled")
        exit(0)

    # Check if Script Exists
    if not disabled_path.is_file():
        print(colored(f"{script} does not exist", "red"))
        raise FileNotFoundError(script)

    # Remove the .d enabling the script
    disabled_path.rename(enabled_path)

@command.command("disable")
@click.argument("script", shell_complete=enabled)
def disable(script: str):
    
    enabled_path = sources_path / script
    disabled_path = sources_path / (script + ".d")

    if (disabled_path.is_file()):
        print("The script is already disabled")
        exit(0)

    # Check if Script Exists
    if not enabled_path.is_file():
        print(colored(f"{script} does not exist", "red"))
        raise FileNotFoundError(script)

    enabled_path.rename(disabled_path)

