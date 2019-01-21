FROM alpine:latest

RUN apk add --no-cache python3
RUN pip3 install pipenv

COPY . /app
WORKDIR /app

RUN pipenv install --system --deploy
RUN pipenv run pytest

RUN for i in $(seq 0 20); do python3 ./main.py "$i"; done

ENTRYPOINT ["python3", "./main.py"]
