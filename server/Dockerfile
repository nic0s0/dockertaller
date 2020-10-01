FROM ubuntu
MAINTAINER nicolas.soto1@mail.udp.cl

EXPOSE 20 21

WORKDIR /server

ARG DEBIAN_FRONTEND=noninteractive

RUN useradd userftp
RUN echo "userftp:passftp" | chpasswd
RUN mkdir serverftp
RUN chmod -R 777 serverftp

RUN apt-get -yqq update \
&& apt-get -yqq install proftpd \
&& apt-get -yqq autoclean

RUN cd /etc/proftpd/ \
&& rm -f proftpd.conf

COPY proftpd.conf /etc/proftpd/proftpd.conf
COPY hola.txt /server/serverftp/

CMD proftpd && tail -f /dev/null
