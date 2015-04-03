FROM postgres:latest

RUN apt-get update
RUN apt-get install -y python-dev python-pip libpq-dev 
RUN pip install peewee psycopg2 ipython faker-factory

ADD . /src
WORKDIR /src
