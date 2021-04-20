tag=duckietown_pondcleaner

regular_packages=duckietown_pondcleaner
test_packages=duckietown_pondcleaner_tests
cover_packages=$(test_packages),$(regular_packages)


CIRCLE_NODE_INDEX ?= 0
CIRCLE_NODE_TOTAL ?= 1

out=out
coverage_dir=$(out)/coverage
tr=$(out)/test-results
xunit_output=$(tr)/nose-$(CIRCLE_NODE_INDEX)-xunit.xml


parallel=--processes=8 --process-timeout=1000 --process-restartworker
coverage=--cover-html --cover-html-dir=$(coverage_dir) --cover-tests --with-coverage --cover-package=$(cover_packages)

xunitmp=--with-xunitmp --xunitmp-file=$(xunit_output)
extra=--rednose --immediate



all:
	@echo "You can try:"
	@echo
	@echo "  make build run"
	@echo "  make docs "
	@echo "  make test coverage-combine coverage-report"
	@echo "  "
	@echo "  make -C notebooks clean all"



black:
	black -l 110 --target-version py37 src

clean:
	coverage erase
	rm -rf $(out) $(coverage_dir) $(tr)

test: clean
	mkdir -p  $(tr)
	DISABLE_CONTRACTS=1 nosetests $(extra) $(coverage)  src  -v --nologcapture $(xunitmp)


test-parallel: clean
	mkdir -p  $(tr)
	DISABLE_CONTRACTS=1 nosetests $(extra) $(coverage) src  -v --nologcapture $(parallel)


test-parallel-circle:
	DISABLE_CONTRACTS=1 \
	NODE_TOTAL=$(CIRCLE_NODE_TOTAL) \
	NODE_INDEX=$(CIRCLE_NODE_INDEX) \
	nosetests $(coverage) $(xunitmp) src  -v  $(parallel)


coverage-combine:
	coverage combine



build:
	docker build -t $(tag) .

build-no-cache:
	docker build --no-cache -t $(tag) .

test-docker: build
	docker run -it $(tag) make test


run:
	mkdir -p out-docker
	docker run -it -v $(PWD)/out-docker:/out $(tag) dt-pc-demo

run-with-mounted-src:
	mkdir -p out-docker
	docker run -it -v $(PWD)/src:/duckietown_pondcleaner/src:ro -v $(PWD)/out-docker:/out $(tag) dt-pc-demo


coverage-report:
	coverage html  -d $(coverage_dir)

docs:
	sphinx-build src $(out)/docs


# Release code

bump-upload:
	$(MAKE) bump
	$(MAKE) upload

bump: # v2
	bumpversion patch
	git push --tags
	git push

upload: # v3
	dts build_utils check-not-dirty
	dts build_utils check-tagged
	dts build_utils check-need-upload --package duckietown-pondcleaner-daffy make upload-do

upload-do:
	rm -f dist/*
	rm -rf src/*.egg-info
	python3 setup.py sdist
	twine upload --skip-existing --verbose dist/*
