# shell completion

import os
import os.path
import sys


def _shell_completion(ctx, option, shell):
    """output shell completion code"""

    if shell is None:
        return
    elif shell == "[auto]":
        if "SHELL" in os.environ:
            shell = os.path.basename(os.environ["SHELL"])
        elif "ZSH_VERSION" in os.environ:
            shell = "zsh"

    if shell not in ["bash", "zsh"]:
        raise RuntimeError("cannot determine shell")

    cli = os.path.basename(ctx.command_path)

    if shell == "bash":
        sys.stderr.write(f"Writing file ~/.{cli}-complete.bash..." + "\n")
        os.system(f"_{cli.upper()}_COMPLETE=bash_source {cli} >~/.{cli}-complete.bash")
        sys.stderr.write("Source this file from ~/.bashrc" + "\n")
        sys.stderr.write(f"ex: . ~/.{cli}-complete.bash" + "\n")

    elif shell == "zsh":
        sys.stderr.write(f"Writing file ~/.{cli}-complete.zsh..." + "\n")
        os.system(f"_{cli.upper()}_COMPLETE=zsh_source {cli} >~/.{cli}-complete.zsh")
        sys.stderr.write("Source this file from ~/.zshrc" + "\n")
        sys.stderr.write(f"ex: . ~/.{cli}-complete.zsh" + "\n")

    sys.exit(0)
