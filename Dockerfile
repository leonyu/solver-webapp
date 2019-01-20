FROM alpine:latest

RUN apk add --no-cache \
        uwsgi-python3 \
        python3

COPY ./app /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./uwsgi.ini /uwsgi.ini

EXPOSE 5000

CMD [ "uwsgi", "--ini", "/uwsgi.ini" ]
