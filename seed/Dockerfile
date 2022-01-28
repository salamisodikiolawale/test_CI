FROM python:3.6.4-alpine3.7

RUN pip install pymongo

COPY seed_mongo.py /

CMD python3 seed_mongo.py
