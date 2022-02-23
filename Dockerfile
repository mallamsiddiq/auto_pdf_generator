

FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /dukkainic


WORKDIR /dukkainic


ADD . /dukkainic/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD gunicorn dukkainic.wsgi:application --bind 0.0.0.0:$PORT