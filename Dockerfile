FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /application/
COPY . .

RUN pip install pipenv
RUN set -ex && pipenv install --deploy --system

CMD [ "uwsgi", "--socket", "0.0.0.0:8330", \
               "--uid", "packreq", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--processes", "8", \
               "--wsgi", "packreq.wsgi:application" ]
