"""Console script for {{cookiecutter.project_slug}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}

import sys
from pathlib import Path
{% if cookiecutter.command_line_interface|lower == 'click' %}
import click
import click.core
{%- endif %}

from .version import __version__, __timestamp__
from .exception_handler import ExceptionHandler

{% if cookiecutter.command_line_interface|lower == 'click' %}
from .shell import _shell_completion
{%- endif %}

header = f"{__name__.split('.')[0]} v{__version__} {__timestamp__}"

{% if cookiecutter.command_line_interface|lower == 'click' %}
def _ehandler(ctx, option, debug):
    ctx.obj = dict(ehandler=ExceptionHandler(debug))
    ctx.obj["debug"] = debug
{%- endif %}


{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.group(context_settings={"auto_envvar_prefix": "{{ cookiecutter.project_cli|upper }}"})
@click.command("{{cookiecutter.project_slug}}")
@click.version_option(message=header)
@click.option("-d", "--debug", is_eager=True, is_flag=True, callback=_ehandler, help="debug mode")
@click.option("--shell-completion", is_flag=True, flag_value="[auto]", callback=_shell_completion, help="configure shell completion")
@click.pass_context
def cli(ctx, debug, shell_completion):
    """{{cookiecutter.project_slug}} top-level help"""
    pass

@cli.command
@click.option("-r", "--raise", type=str, show_envvar=True, help='example option')
@click.option("-f", "--flag", is_flag=True, help='example flag option')
@click.option("-i", "--input-file", type=click.Path(dir_okay=False, readable=True, exists=True, path_type=Path), help="input file")
@click.option("-o", "--output-file", type=click.Path(dir_okay=False, writable=True, exists=False, path_type=Path), help="output file")
@click.argument('input', click.File('r'))
@click.argument('output', click.File('w'), required=False, default='-')
@click.pass_context
def action(ctx, raise, flag, input_file, output_file, input, output):
    """action command help"""

    if raise == "exception":
        raise RuntimeError(option)

{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def cli():
    """Console script for {{cookiecutter.project_slug}}."""
    print(header)
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    raise RuntimeError("Add application code to {{cookiecutter.project_slug}}/cli.py")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
