FROM python:3.9-slim

EXPOSE 5000

RUN mkdir /app
COPY config.yaml api.py *.pkl requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

CMD python api.py