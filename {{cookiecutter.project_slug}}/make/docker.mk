#
# docker makefile
#
 
$(if $(DOCKER_REGISTRY),,$(error DOCKER_REGISTRY is undefined))

registry = $(DOCKER_REGISTRY)
base_version = $(shell repo-release seven-testnet)

base_image = debian:11
image_tag = $(registry)/$(project)
image = $(image_tag):latest

build_opts = \
 --build-arg BASE_IMAGE=$(base_image) \
 --build-arg VERSION=$(version) \
 --tag $(image_tag) \
 --progress plain

docker_deps = $(wildcard docker/*) docker/VERSION
	
cleanup_files := docker/.build docker/VERSION docker/*.whl

docker/VERSION: VERSION
	cp $< $@

### build image
build: depends docker/.build

docker/.build: $(docker_deps) 
	docker build $(build_opts) docker | tee build.log
	docker tag $(image) $(image_tag):$(version)
	touch $@

### rebuild image
rebuild: clean depends
	$(MAKE) build_opts="$(build_opts) --no-cache" build

### docker-clean
docker-clean:
	rm -rf $(cleanup_files)

### docker-sterile
docker-sterile: docker-clean


### push image to docker registry
push: build release
	docker push $(image_tag):$(version)
	docker push $(image)
