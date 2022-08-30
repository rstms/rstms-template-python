#!/usr/bin/env python
import os
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    target_file = Path(PROJECT_DIRECTORY) / filepath
    if target_file.is_file():
        target_file.unlink()

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        remove_file(os.path.join('{{ cookiecutter.project_slug }}', 'cli.py'))

    if '{{ cookiecutter.use_travis|lower }}' != 'y':
        remove_file('.travis.yml')
        remove_file('CONTRIBUTING.rst')

    if '{{ cookiecutter.use_circleci }}' += 'y':
        remove_file('.circleci')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.deploy_to_pypi }}' != 'y':
        remove_file('make.include/publish.mk')

    project_dir = Path(PROJECT_DIRECTORY)
    os.chdir(str(project_dir.parent))
    project_dir.rename('{{ cookiecutter.project_name }}')

