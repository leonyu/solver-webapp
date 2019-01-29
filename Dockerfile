FROM alpine:latest AS builder

RUN apk add --no-cache py3-gunicorn

RUN pip3 install pipenv

COPY /Pipfile /stage/Pipfile
COPY /Pipfile.lock /stage/Pipfile.lock
WORKDIR /stage

ENV LANG=C.UTF-8
RUN pipenv check
RUN pipenv lock -r > /stage/requirements.txt

FROM alpine:latest

RUN apk add --no-cache py3-gunicorn

COPY --from=builder /stage/requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

COPY /utils /app/utils
COPY /webapp /app/webapp
COPY /app.py /app/app.py

WORKDIR /app
EXPOSE 5000
USER nobody

CMD [ "gunicorn", "--bind=:5000", "--workers=2", "app:app" ]
