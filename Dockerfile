FROM python:3.6.9-alpine

EXPOSE 8000

RUN mkdir -p /app
WORKDIR /app

CMD [ "python", "-u", "music_store_app.py" ]

COPY . /app
