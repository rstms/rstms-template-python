#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` CLI"""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}

{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }} import __version__

{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.project_slug }} import cli
{%- endif %}

{%- if cookiecutter.use_pytest == 'y' %}

def test_version():
    """Test reading version and module name"""
    assert {{ cookiecutter.project_slug }}.__name__ == "{{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}"
    assert __version__
    assert isinstance(__version__, str)

{%- if cookiecutter.command_line_interface|lower == 'click' %}

@pytest.fixture
def run():
    runner = CliRunner()

    #env = os.environ.copy()
    #env['EXTRA_ENV_VAR'] = 'VALUE'

    def _run(cmd, **kwargs):
        expected_exit = kwargs.pop("expected_input", 0)
        #kwargs["env"] = env
        result = runner.invoke(cli, cmd, **kwargs)
        if result.exception:
            print_exception(result.exception)
            breakpoint()
            pass
        assert result.exit_code == expected_exit, result.output
        return result.output

    return _run

def test_cli(run):
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output

def test_help(run):
    output = run(['--help'])
    assert '--help  Show this message and exit.' in output

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
