#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        remove_file(os.path.join('{{ cookiecutter.project_slug }}', 'cli.py'))

    if 'no' in '{{ cookiecutter.use_travis|lower }}':
        remove_file('.travis.yml')
        remove_file('CONTRIBUTING.rst')

    if 'no' in '{{ cookiecutter.use_circleci|lower }}':
        remove_file('.circleci')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if 'no' in '{{ cookiecutter.deploy_to_pypy|lower }}':
        remove_file(os.path.join('{{ make.include }}', 'publish.mk'))
