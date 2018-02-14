FROM python:2-alpine
COPY . /app
WORKDIR /app
RUN for i in $(seq 0 20); do ./main.py "$i"; done

ENTRYPOINT ["./main.py"]
CMD []
