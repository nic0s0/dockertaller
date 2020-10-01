FROM ubuntu
MAINTAINER nicolas.soto1@mail.udp.cl

EXPOSE 20 21

RUN apt-get update \
&& apt-get install -yqq lftp \
&& apt-get -yqq autoclean

CMD ["lftp", "userftp:passftp@172.17.0.2"]
