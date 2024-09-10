# syntax=docker/dockerfile:1
FROM python:3.11-alpine
COPY . /server
WORKDIR /server
RUN pip install pymodbustcp
WORKDIR /server
EXPOSE 502
ENTRYPOINT [ "python", "server.py" ]

