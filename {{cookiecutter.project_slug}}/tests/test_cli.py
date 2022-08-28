#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` CLI"""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}
from traceback import print_exception

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

    #env = os.environ.copy()
    #env['EXTRA_ENV_VAR'] = 'VALUE'

    def _run(cmd, **kwargs):
        expect_exit_code = kwargs.pop("expect_exit_code", 0)
        expect_exception = kwargs.pop("expect_exception", None)
        #kwargs["env"] = env
        result = runner.invoke(cli, cmd, **kwargs)
        if result.exception:
            if not isinstance(result.exception, expect_exception):
                print_exception(result.exception)
                breakpoint()
                pass
        else:
            assert result.exit_code == expect_exit_code, result.output
        return result

    return _run

def test_cli(run):
    """Test the CLI."""
    result = run([], expect_exception=RuntimeError)
    assert '{{ cookiecutter.project_slug }}/cli.py' in str(result.exception)

def test_help(run):
    result = run(['--help'])
    assert 'Show this message and exit.' in result.output

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
