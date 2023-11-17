FROM python:3.8.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /admin

RUN pip install -U pip
RUN pip install -U setuptools
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /admin
