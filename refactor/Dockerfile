FROM python:3.6.9-alpine

EXPOSE 8000

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /app
CMD [ "python", "-u", "main.py" ]


