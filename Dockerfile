FROM python:3.9.7-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python3 -m venv /opt/venv

RUN opt/venv/bin/pip install --upgrade pip

COPY ./requirements.txt .
RUN opt/venv/bin/pip install -r requirements.txt

COPY ./src /app

WORKDIR /app

COPY ./entrypoint.sh /

ENTRYPOINT [ "sh", "/entrypoint.sh" ]