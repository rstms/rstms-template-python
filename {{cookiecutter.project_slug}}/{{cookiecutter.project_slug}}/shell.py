# shell completion

from os import environ, system

import click


def _shell_completion(shell):
    """output shell completion code"""
    if shell == "[auto]":
        if "ZSH_VERSION" in environ:
            shell = "zsh"
        else:
            shell = "bash"
    if shell not in ["bash", "zsh"]:
        raise RuntimeError("cannot determine shell")

    cli="{{cookiecutter.project_cli}}"

    if shell == "bash":
        click.echo(f"Writing file ~/.{cli}-complete.bash...")
        system(f"_{cli.upper()}_COMPLETE=bash_source {cli} >~/.{cli}-complete.bash")
        click.echo("Source this file from ~/.bashrc")
        click.echo(f"ex: . ~/.{cli}-complete.bash")

    elif shell == "zsh":
        click.echo(f"Writing file ~/.{cli}-complete.zsh...")
        system(f"_{cli.upper()}_COMPLETE=zsh_source {cli} >~/.{cli}-complete.zsh")
        click.echo("Source this file from ~/.zshrc")
        click.echo(f"ex: . ~/.{cli}-complete.zsh")
