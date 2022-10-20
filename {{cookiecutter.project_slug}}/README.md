{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
![Image](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{% if (cookiecutter.use_pypi_deployment_with_travis == 'y') or (cookiecutter.deploy_to_pypi == 'y') %}
![Image](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)
{%- endif %}
{% if (cookiecutter.use_pypi_deployment_with_travis == 'y')  or (cookiecutter.use_travis == 'y') %}
![Image](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg)
{%- endif %}
{% if cookiecutter.use_circleci == 'y' %}
![Image](https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tree/master.svg?style=shield)
{%- endif %}
{% if cookiecutter.use_readthedocs_io == 'y' %}
![Image](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)
{%- endif %}
{% if cookiecutter.add_pyup_badge == 'y' %}
![Image](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg)
{%- endif %}
{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}


Credits
-------

This package was created with Cookiecutter and `rstms/cookiecutter-python-cli`, a fork of the `audreyr/cookiecutter-pypackage` project template.

[audreyr/cookiecutter](https://github.com/audreyr/cookiecutter)
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
[rstms/cookiecutter-python-cli](https://github.com/rstms/cookiecutter-python-cli)
