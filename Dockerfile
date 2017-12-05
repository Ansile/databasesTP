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

RUN apt-get install -y postgresql-contrib-$POSTGRESV

USER postgres

RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER ansile WITH SUPERUSER PASSWORD '123456789';" &&\
    createdb -E UTF8 -T template0 -O ansile technopark &&\
    /etc/init.d/postgresql stop

RUN echo "host all  all    0.0.0.0/0  trust" >> /etc/postgresql/$POSTGRESV/main/pg_hba.conf

RUN echo "listen_addresses='*'" >> /etc/postgresql/$POSTGRESV/main/postgresql.conf
RUN echo "synchronous_commit=off" >> /etc/postgresql/$POSTGRESV/main/postgresql.conf

EXPOSE 5432

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

USER root

ADD tornado_api/ $WORKDIR/tornado_api/
ADD DBSchema.sql $WORKDIR/DBSchema.sql

RUN echo "Europe/Moscow" > /etc/timezone

EXPOSE 5000
ENV TZ Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV PGPASSWORD 123456789
CMD service postgresql start &&\
    cd $WORKDIR/ &&\
    psql -h localhost -U ansile -d technopark -f DBSchema.sql -w &&\
    cat /etc/timezone &&\
    date &&\
    # pg_dump -h localhost -U ansile -c technopark &&\
    python3 ./tornado_api/start.py
