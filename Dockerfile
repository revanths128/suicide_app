FROM python:3.12.0a3-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT FLASK_APP=./app.py flask run --host=0.0.0.0 --port=3000