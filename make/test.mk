test: test-${TARGET}

test-docker: ${VERSION} requirements.install
	${SCRIPTS_DIR}/docker_test.sh

test-local: ${VERSION} requirements.install
	@pip install -e .
	@python setup.py test

test-ci: test-local

test-production:
