FROM alpine:3.11 AS builder
RUN apk add --no-cache py3-gunicorn

RUN pip3 install pipenv

COPY / /stage
WORKDIR /stage

ENV LANG=C.UTF-8
RUN pipenv install --dev
RUN pipenv check
RUN pipenv run pylint utils webapp tests
RUN pipenv run mypy --strict utils webapp tests
RUN pipenv run pytest
RUN pipenv lock -r > /stage/requirements.txt

FROM alpine:3.11
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
