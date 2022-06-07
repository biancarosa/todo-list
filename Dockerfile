FROM python:3.10.5-alpine

RUN apk add --no-cache --update git make gcc python3-dev musl-dev build-base
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD app app

CMD exec gunicorn app.main:app