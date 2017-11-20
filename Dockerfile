FROM ubuntu:16.04

RUN apt-get -y update

ENV POSTGRESV 9.5
RUN apt-get install -y postgresql-$POSTGRESV

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

ENV WORKDIR ./
ADD requirements.txt $WORKDIR/requirements.txt

RUN pip3 install -r requirements.txt

USER postgres

RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -E UTF8 -T template0 -O docker docker &&\
    /etc/init.d/postgresql stop

RUN echo "host all  all    0.0.0.0/0  trust" >> /etc/postgresql/$POSTGRESV/main/pg_hba.conf

RUN echo "listen_addresses='*'" >> /etc/postgresql/$POSTGRESV/main/postgresql.conf
RUN echo "synchronous_commit=off" >> /etc/postgresql/$POSTGRESV/main/postgresql.conf

EXPOSE 5432

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

USER root

ADD tornado_api/ $WORKDIR/tornado_api/
ADD DBSchema.sql $WORKDIR/DBSchema.sql

EXPOSE 5000

ENV POSTGRESPWD docker
CMD service postgresql start &&\
    cd $WORKDIR/ &&\
    psql -h localhost -U docker:docker -d docker -f DBSchema.sql -w &&\
    gunicorn -b :5000 main:app