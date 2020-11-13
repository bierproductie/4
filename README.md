# MCT Axle Counter API

[![Technical Debt](https://software.siemens.dk/mo-sonar/api/project_badges/measure?branch=conform-to-new-architecture-fast-api&project=bierproductie_api&metric=sqale_index)](https://software.siemens.dk/mo-sonar/dashboard?id=bierproductie_api&branch=conform-to-new-architecture-fast-api)
[![Vulnerabilities](https://software.siemens.dk/mo-sonar/api/project_badges/measure?branch=conform-to-new-architecture-fast-api&project=bierproductie_api&metric=vulnerabilities)](https://software.siemens.dk/mo-sonar/dashboard?id=bierproductie_api&branch=conform-to-new-architecture-fast-api)
[![Coverage](https://software.siemens.dk/mo-sonar/api/project_badges/measure?branch=conform-to-new-architecture-fast-api&project=bierproductie_api&metric=coverage)](https://software.siemens.dk/mo-sonar/dashboard?id=bierproductie_api&branch=conform-to-new-architecture-fast-api)
[![Duplicated Lines (%)](https://software.siemens.dk/mo-sonar/api/project_badges/measure?branch=conform-to-new-architecture-fast-api&project=bierproductie_api&metric=duplicated_lines_density)](https://software.siemens.dk/mo-sonar/dashboard?id=bierproductie_api&branch=conform-to-new-architecture-fast-api)
[![Reliability Rating](https://software.siemens.dk/mo-sonar/api/project_badges/measure?branch=conform-to-new-architecture-fast-api&project=bierproductie_api&metric=reliability_rating)](https://software.siemens.dk/mo-sonar/dashboard?id=bierproductie_api&branch=conform-to-new-architecture-fast-api)
[![Security Rating](https://software.siemens.dk/mo-sonar/api/project_badges/measure?branch=conform-to-new-architecture-fast-api&project=bierproductie_api&metric=security_rating)](https://software.siemens.dk/mo-sonar/dashboard?id=bierproductie_api&branch=conform-to-new-architecture-fast-api)

*Restful API for MCT Axle Counter based on the
[Open API 3.0 specification](https://swagger.io/specification/)*

### Tech stack
- [FastAPI](https://fastapi.tiangolo.com)
- [PostgreSQL](https://www.postgresql.org)
- [Gino](https://python-gino.org)
- [Docker](https://www.docker.com)


##### Hot reloading

By default hot reloading is enabled, so when you execute `make run` (regardless
of that being Docker or local (native)) the program will auto update given you
don't introduce new external packages.

##### Swagger UI and ReDoc
Interactive documentation can be reached at [localhost:11001/docs](localhost:11001/docs)
(for Swagger UI) and [localhost:11001/redoc](localhost:11001/redoc) for ReDoc.
