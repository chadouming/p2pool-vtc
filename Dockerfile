# Dockerfile for P2Pool Server

FROM debian:10-slim

LABEL maintainer Chad Cormier Roussel <chadcormierroussel@gmail.com>
LABEL description="Dockerized P2Pool (VTC)"

WORKDIR /p2pool
ENV P2POOL_REPO https://github.com/chadouming/p2pool-vtc.git
ENV P2POOL_BRANCH master

# update container and install dependencies
RUN apt-get -y update \
  && apt-get install -y python3 python3-rrdtool python3-pygame python3-scipy python3-twisted python3-pil python3-setuptools python3-pip git make nano wget  \
  && apt-get clean

ADD src/init.sh /init.sh
RUN chmod +x /init.sh

RUN mkdir /src

WORKDIR /src/
RUN git clone --depth 1 --branch $P2POOL_BRANCH $P2POOL_REPO

WORKDIR /src/p2pool-vtc/
RUN git submodule update --init --recursive
RUN git submodule update --recursive

WORKDIR /src/p2pool-vtc/verthash-pospace
RUN make all
RUN python3 setup.py install

WORKDIR /src/p2pool-vtc/
RUN python3 setup.py install

# create configuration volume
VOLUME /config /data

# default environment variables
ENV RPC_USER user
ENV RPC_PASSWORD changethisfuckingpassword
ENV VERTCOIND_HOST 127.0.0.1
ENV VERTCOIND_HOST_PORT 5888
ENV FEE 0
ENV MAX_CONNECTIONS 50
ENV FEE_ADDRESS VnfNKCy5Aq7vZq5W9UKgMwfDLT7NrPRWZK
ENV NET vertcoin

# expose mining port
EXPOSE 9171 9181 9346 9347

ENTRYPOINT ["/init.sh"]
