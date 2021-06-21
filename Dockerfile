# Dockerfile for P2Pool Server

FROM debian:10-slim

LABEL maintainer Chad Cormier Roussel <chadcormierroussel@gmail.com>
LABEL description="Dockerized P2Pool (VTC)"

WORKDIR /p2pool
ENV P2POOL_REPO https://github.com/chadouming/p2pool-vtc.git
ENV P2POOL_BRANCH v3.1.0

# update container and install dependencies
RUN apt-get -y update \
  && apt-get install -y python python-rrdtool python-pygame python-scipy python-twisted python-twisted-web python-pil python-setuptools python-pip git make nano wget  \
  && apt-get clean

ADD src/init.sh /init.sh
RUN chmod +x /init.sh

RUN mkdir /src

WORKDIR /src
RUN cd /src && git clone https://github.com/vertcoin-project/verthash-pospace

WORKDIR /src/verthash-pospace/tiny_sha3
RUN git submodule init
RUN git submodule update

WORKDIR /src/verthash-pospace
RUN make all
RUN python setup.py install

WORKDIR /src/
RUN git clone --depth 1 --branch $P2POOL_BRANCH $P2POOL_REPO

WORKDIR /src/p2pool-vtc/
RUN pip install -r requirements.txt

WORKDIR /src/p2pool-vtc/lyra2re-hash-python/
RUN git submodule init
RUN git submodule update

WORKDIR /src/p2pool-vtc/web-static/
RUN git submodule init
RUN git submodule update

WORKDIR /src/p2pool-vtc/
RUN python setup.py install

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
