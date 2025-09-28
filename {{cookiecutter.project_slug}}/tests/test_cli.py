# cli tests

import os
import shlex

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}

import {{ cookiecutter.project_slug }}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.project_slug }} import __version__, cli
from click.testing import CliRunner
{% else %}
from {{ cookiecutter.project_slug }} import __version__
{%- endif %}

{%- if cookiecutter.use_pytest == 'y' %}

def test_version():
    """Test reading version and module name"""
    assert {{ cookiecutter.project_slug }}.__name__ == "{{ cookiecutter.project_slug }}"
    assert __version__
    assert isinstance(__version__, str)

{%- if cookiecutter.command_line_interface|lower == 'click' %}

@pytest.fixture
def run():
    runner = CliRunner()

    env = os.environ.copy()
    env['TESTING'] = '1'

    def _run(cmd, **kwargs):
        assert_exit = kwargs.pop("assert_exit", 0)
        assert_exception = kwargs.pop("assert_exception", None)
        env.update(kwargs.pop("env", {}))
        kwargs["env"] = env
        result = runner.invoke(cli, cmd, **kwargs)
        if assert_exception is not None:
            assert isinstance(result.exception, assert_exception)
        elif result.exception is not None:
            raise result.exception from result.exception
        elif assert_exit is not None:
            assert result.exit_code == assert_exit, (
                f"Unexpected {result.exit_code=} (expected {assert_exit})\n"
                f"cmd: '{shlex.join(cmd)}'\n"
                f"output: {str(result.output)}"
            )
        return result

    return _run

def test_cli_no_args(run):
    result = run([], assert_exception=SystemExit)
    assert "Usage:" in result.output

def test_cli_help(run):
    result = run(['--help'])
    assert 'Show this message and exit.' in result.output

def test_cli_exception(run):

    cmd = ["--shell-completion", "and_now_for_something_completely_different"]

    with pytest.raises(RuntimeError) as exc:
        result = run(cmd)
    assert isinstance(exc.value, RuntimeError)

    # example of testing for expected exception
    result = run(cmd, assert_exception=RuntimeError)
    assert result.exception
    assert result.exc_info[0] == RuntimeError
    assert result.exception.args[0] == "cannot determine shell"

    with pytest.raises(AssertionError) as exc:
        result = run(cmd, assert_exception=ValueError)
    assert exc


def test_cli_exit(run):
    result = run(["--help"], assert_exit=None)
    assert result
    result = run(["--help"], assert_exit=0)
    assert result
    with pytest.raises(AssertionError):
        run(['--help'], assert_exit=-1)

{%- endif %}

{%- else %}

class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

{%- if cookiecutter.command_line_interface|lower == 'click' %}

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

{%- endif %}

{%- endif %}
