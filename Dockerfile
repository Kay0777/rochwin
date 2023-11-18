FROM python:3.8.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /admin/requirements.txt
COPY admin /admin

WORKDIR /admin

RUN pip install -U pip setuptools
RUN pip install -r /admin/requirements.txt
