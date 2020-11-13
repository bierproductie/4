install: install-${TARGET}

install-docker: ${VERSION} requirements.install
	@docker-compose build

install-local: ${VERSION} requirements.install
	@pip install \
		-e '.[dev]'

install-ci: install-local

install-production:
	# TODO(Rathka: This should install inside a virtual env.)
	# Assume that we are inside a venv.
	# run scripts/generate_deployment_resources.sh might need venv arg (something like that)
	# pip install .
