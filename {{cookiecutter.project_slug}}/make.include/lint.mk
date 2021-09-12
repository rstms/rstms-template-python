# lint / source format
{%- if cookiecutter.formatter == 'yapf' %}
# yapf - source formatter
 
# run the yapf formatter on any sources changed since the last run
fmt: .fmt .style.yapf  
.fmt: $(python_src)
	@$(foreach s,$?,yapf -i -vv $(s) || exit;) 
	@touch $@

# if necessary, create a default .style.yapf and customize by applying $(yapf_rules)
.style.yapf:
	echo '[style]'>$@
	$(foreach rule,$(yapf_rules),echo '$(rule)' >>$@;)
	yapf --no-local-style --style-help | \
	sed '/^\s*\[style\]/d' | \
	sed '/^\s*#/d' | \
	sed '/^\s*$$/d'| \
        $(foreach rule,$(yapf_rules),sed '$(call sed_delete_rule,$(rule))' |) \
	sort >>$@

# remove version marker, forcing reformat of all python source 
fmt-clean:
	rm -f .fmt
	rm -r .style.yapf

sed_delete_rule = /^\s*$(firstword $(subst =, ,$(1)))\s*=.*$$/d

define yapf_rules
allow_split_before_dict_value=False
arithmetic_precedence_indication=True
blank_line_before_nested_class_or_def=True
coalesce_brackets=True
column_limit=130
dedent_closing_brackets=True
indent_dictionary_value=True
join_multiple_lines=False
spaces_before_comment=4
split_before_arithmetic_operator=True
split_before_dot=True
split_before_expression_after_opening_paren=True
split_before_first_argument=True
endef
{%- endif %}

{%- if cookiecutter.use_lint == 'y' %}
lint: ## check style with flake8
	flake8 $(project) tests
	{% if cookiecutter.formatter == 'black' %}
	black --check $(project) tests
	{%- endif %}
{%- endif %}

{%- if cookiecutter.formatter == 'black' %}
fmt: ## blacken python sources
	black $(project) tests
{%- endif %}

# vim:ft=make
