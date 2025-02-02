# python dependency wheels


.depends: $(dep_wheels)
	$(foreach depmod,$(common_modules),$(call github-download,$(depmod));)
	@touch $@
	
depends: .depends

depends-clean: dist-clean
	rm -f .depends

depends-sterile:
	@:

depends-ls:
	@$(foreach wheel,$(dep_wheels),ls -l $(wheel);)

github-download = gh -R $(GITHUB_ORG)/$(1) release download --clobber -D dist -p '*.whl'
