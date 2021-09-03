FROM python:3.7

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./connector ./connector

WORKDIR ./connector

ENTRYPOINT ["python", "start_connection.py"]
