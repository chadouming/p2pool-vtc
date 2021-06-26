#! /bin/bash

# generate vertcoin.conf
## TODO -> Change /root/.vertcoin/vertcoin.conf to /config/vertcoin.conf

# create directory if it doesn't exist
if [ ! -d /root/.vertcoin ]; then
  mkdir /root/.vertcoin
fi

ln -s /data/verthash.dat verthash.dat

# create the file whether it exists or not
cat <<EOF > /root/.vertcoin/vertcoin.conf
  server=1
  rpcuser=$RPC_USER
  rpcpassword=$RPC_PASSWORD
EOF

# Set the worker port for the correct network
# If network 1, 9171, if network2 9181, default to 9181 for now

if [ $NET = 'vertcoin' ]; then
  export WORKER_PORT=9171
elif [ $NET = 'vertcoin2' ]; then
  export WORKER_PORT=9181
else
  export WORKER_PORT=9181
fi

python3 /src/p2pool-vtc/run_p2pool.py --debug --net $NET --datadir /data -f $FEE --bitcoind-address $VERTCOIND_HOST --bitcoind-rpc-port $VERTCOIND_HOST_PORT --max-conns $MAX_CONNECTIONS -a $FEE_ADDRESS --p2pool-port 9346 --worker-port $WORKER_PORT
