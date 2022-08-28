#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{%- else %}
import unittest
{%- endif -%}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.project_slug }} import __version__{% if cookiecutter.command_line_interface|lower == 'click' %}, cli{% endif %}, {{ cookiecutter.project_slug }}

{%- if cookiecutter.use_pytest == 'y' %}


def test_version():
    """Test reading version and module name"""
    assert {{ cookiecutter.project_slug }}.__name__ == "{{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}"
    assert __version__
    assert isinstance(__version__, str)

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



def test_cli():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code != 0, result
    assert result.exception, result
    assert "{{ cookiecutter.project_slug }}" in str(result.exception), result

    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0, result
    assert "Show this message and exit." in result.output, result
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
        result = runner.invoke(cli)
        assert result.exit_code != 0, result
        assert result.exception, result
        assert "{{ cookiecutter.project_slug }}.cli" in str(result.exception), result
        help_result = runner.invoke(cli, ["--help"])
        assert help_result.exit_code == 0, result
        assert "--help  Show this message and exit." in help_result.output, result
{%- endif %}
{%- endif %}
