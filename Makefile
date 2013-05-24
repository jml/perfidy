# See LICENSE for copyright and licensing details.

PACKAGE_NAME=perfidy
PROJECT_URL=https://github.com/jml/perfidy
PYTHON=python
SOURCES=$(shell find ${PACKAGE_NAME} -name "*.py")

check:
	PYTHONPATH=$(PWD) $(PYTHON) -m testtools.run perfidy.tests.test_suite

TAGS: ${SOURCES}
	ctags -e -R ${PACKAGE_NAME}/

tags: ${SOURCES}
	ctags -R ${PACKAGE_NAME}/

clean:
	rm -f TAGS tags
	find ${PACKAGE_NAME} -name "*.pyc" -exec rm '{}' \;

### Documentation ###

apidocs:
	# pydoctor emits deprecation warnings under Ubuntu 10.10 LTS
	PYTHONWARNINGS='ignore::DeprecationWarning' \
		pydoctor --make-html --add-package extras \
		--docformat=restructuredtext --project-name=${PACKAGE_NAME} \
		--project-url=${PROJECT_URL}


.PHONY: apidocs
.PHONY: check clean
