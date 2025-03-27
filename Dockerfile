# syntax = docker/dockerfile:1.6

FROM golang:1.22-alpine3.20 AS dev
WORKDIR /build

ADD https://github.com/cybardev/ytgo.git /build/
RUN go build -C cmd/ytgo -o ytgo

FROM python:3.12-alpine3.20 AS main
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=dev /build/cmd/ytgo/ytgo /bin/ytgo
COPY bot.py utils.py ./

EXPOSE 10000
CMD [ "python", "bot.py" ]
