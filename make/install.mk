install: install-${TARGET}

install-docker: ${VERSION} requirements.install
    @docker-compose build

install-local: ${VERSION} requirements.install
    @pip install -e '.[dev]'

install-ci: install-local
