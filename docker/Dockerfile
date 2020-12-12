## base image
FROM python:slim-buster AS compile-image

## install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential curl

RUN addgroup --gid 1000 bierproductie
RUN adduser --home /home/bierproductie --uid 1000 --gid 1000 --disabled-password bierproductie
USER bierproductie
WORKDIR /home/bierproductie

## virtualenv
ENV VIRTUAL_ENV=/home/bierproductie/.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip

RUN mkdir bierproductie_api
WORKDIR /home/bierproductie/bierproductie_api

## add and install requirements
COPY --chown=bierproductie:bierproductie requirements.install .
RUN pip install -r requirements.install

## copy over rest of the app
COPY --chown=bierproductie:bierproductie . .

RUN pip install -e '.[dev]'

ENTRYPOINT ["./docker/entrypoint.sh"]
