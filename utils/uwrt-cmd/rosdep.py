import click
import os

@click.command("rosdep", short_help="Install ROS Dependencies")
@click.argument("path", required=False, default=".")
def command(path):
    """
    Searches a PATH for ROS packages installing dependencies
    found in package.xml.

    Arguments:

        PATH        Path to search for packages     Default: .
    """

    os.execlp("rosdep", "rosdep", "install", "-yri", "--from-paths", path)
