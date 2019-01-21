FROM alpine:latest

RUN apk add --no-cache \
        uwsgi-python3 \
        python3

RUN pip3 install pipenv

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN pipenv install --system --deploy

COPY uwsgi.ini /uwsgi.ini
EXPOSE 5000

COPY ./app /app
WORKDIR /app

CMD [ "uwsgi", "--ini", "/uwsgi.ini" ]
