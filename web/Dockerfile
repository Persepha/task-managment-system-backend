FROM python:3.12.7-slim

# Fix python printing
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN python3 -m  venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade &&  \
    /opt/venv/bin/pip install -r requirements-dev.txt