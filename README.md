# Bierproductie API

### Docs
https://api.bierproductie.nymann.dev/docs

https://api.bierproductie.nymann.dev/redoc

### How to deploy
It's recommended to run the Bierproductie API via docker and docker-compose.
The docker image is hosted on my private repository (registry.nymann.dev), but
an example docker-compose.yml file can be found in the root directory.


### How to setup a development environment
If you are on a Linux based os you can utilise the provided `make` targets.
`make run`, `make test`. Is both being run via docker, but by appending `-local`
to the end of the commands (fx. `make run-local`) it will run on the metal.
Note that you have to setup a database (look in `.env` for credentials).
After you have created a database, run `alembic upgrade head` from the root
directory.
