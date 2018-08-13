FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /application/
COPY . .

RUN pip install pipenv
RUN set -ex && pipenv install --deploy --system
