FROM python:3.10-slim-bullseye

ENV WORKSPACE=/usr/src/app

RUN mkdir -p $WORKSPACE
WORKDIR $WORKSPACE

COPY . $WORKSPACE

RUN pip install --upgrade pipenv

RUN pipenv install --dev