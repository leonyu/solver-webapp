FROM alpine:latest

RUN apk add --no-cache python3
RUN pip3 install pipenv

COPY . /app
WORKDIR /app

RUN pipenv install --system --deploy

EXPOSE 5000

CMD [ "gunicorn", "run:app" ]
