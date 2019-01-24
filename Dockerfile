FROM alpine:latest

RUN apk add --no-cache python3

COPY . /app
WORKDIR /app

RUN for i in $(seq 0 20); do python3 ./main.py "$i"; done

CMD ["python3", "./main.py"]
