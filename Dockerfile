FROM alpine:latest

RUN apk add --no-cache \
        uwsgi-python3 \
        python3

RUN pip3 install pipenv

COPY . /app
WORKDIR /app

RUN pipenv install --system --deploy

EXPOSE 5000

CMD [ "uwsgi", "--ini", "/app/uwsgi.ini" ]
