FROM python:2.7

RUN apt-get update \
    && apt-get install -y coreutils \
    && rm -rf /var/lib/apt/lists/*
