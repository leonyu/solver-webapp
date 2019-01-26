FROM alpine:latest

RUN apk add --no-cache python3
RUN pip3 install pipenv

COPY /Pipfile /app/Pipfile
COPY /Pipfile.lock /app/Pipfile.lock
WORKDIR /app

RUN pipenv install --system --deploy

COPY /util /app/util
COPY /webapp /app/webapp
COPY /run.py /app/run.py

EXPOSE 5000

USER nobody

CMD [ "gunicorn", "--bind=:5000", "--workers=2", "run:app" ]
