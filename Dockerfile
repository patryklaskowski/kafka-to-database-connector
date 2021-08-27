FROM python:3.7

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./kafkacons_dbinsert ./kafkacons_dbinsert

#ENV PYTHONPATH="$PYTHONPATH:/kafkacons_dbinsert"
WORKDIR ./kafkacons_dbinsert

ENTRYPOINT ["python", "kafkacons_dbinsert.py"]
