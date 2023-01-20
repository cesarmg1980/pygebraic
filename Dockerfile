FROM python:3.9

RUN mkdir /app 
COPY . /app

WORKDIR /app 

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN python -m pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
