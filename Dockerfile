FROM alpine:latest

RUN apk add --no-cache \
        uwsgi-python3 \
        python3

COPY ./app /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "uwsgi", "--socket", "0.0.0.0:5000", \
               "--uid", "uwsgi", "--master", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "main:application" ]
