FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip install pipenv && pipenv install --deploy --system --ignore-pipfile

RUN useradd -s /bin/bash admin
USER admin
