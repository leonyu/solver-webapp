FROM alpine:latest

RUN apk add --no-cache python3
RUN pip3 install pipenv

COPY . /app
WORKDIR /app

RUN pip3 install nose
RUN nosetests

RUN for i in $(seq 0 20); do python3 ./main.py "$i"; done

ENTRYPOINT ["python3", "./main.py"]
