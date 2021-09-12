# lint / source format

{%- if cookiecutter.use_black == 'y' %}
fmt:  ## blacken python source
	black $(project) tests
{%- endif %}

lint:{% if cookiecutter.use_black == 'y' %} fmt{%- endif %}  ## check style with flake8
	flake8 $(project) tests
{% if cookiecutter.use_black == 'y' %}
	black --check $(project) tests
{%- endif %}

# vim:ft=make
