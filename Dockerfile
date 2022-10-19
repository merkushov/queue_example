FROM python:3.9.12

ENV PYTHONUNBUFFERED=0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
