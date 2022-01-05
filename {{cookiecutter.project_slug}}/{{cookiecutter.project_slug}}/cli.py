"""Console script for {{cookiecutter.project_slug}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}

import sys
{% if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command("{{cookiecutter.project_slug}}")
@click.version_option()
@click.option("-d", "--debug", is_flag=True, help="debug mode")
def cli(debug):

    def exception_handler(
        exception_type, exception, traceback, debug_hook=sys.excepthook
    ):

        if debug:
            debug_hook(exception_type, exception, traceback)
        else:
            click.echo(f"{exception_type.__name__}: {exception}", err=True)

    sys.excepthook = exception_handler

    """cli for {{cookiecutter.project_slug}}."""
    raise RuntimeError("Add application code to {{cookiecutter.project_slug}}/cli.py")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into {{cookiecutter.project_slug}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
