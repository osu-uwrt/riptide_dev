#!/bin/env python3

import click

command = click.Group("env")
command.short_help = "Test Help"

@click.command("enable")
def enable():
    print("Enable")

command.add_command(enable)
