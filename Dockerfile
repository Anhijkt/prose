FROM python:3.6-alpine

WORKDIR /home/prose

RUN apk add build-base

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app app
COPY migrations migrations
COPY config.py config.py
COPY data.sqlite data.sqlite
COPY prose.py prose.py
COPY boot.sh boot.sh 
EXPOSE 5000

ENTRYPOINT ["./boot.sh"]