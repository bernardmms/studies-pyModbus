# syntax=docker/dockerfile:1
FROM python:3.11-alpine
COPY . /client
WORKDIR /client
RUN pip install pymodbustcp
RUN ls -la /client
EXPOSE 502
ENTRYPOINT [ "python", "client.py" ]
