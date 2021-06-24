**P2pool installation with Docker -- Linux**


To have this docker running, you will need 2 things.
A vertcoind node and patience.


To get the vertcoind node, the easy way is to use this command

```bash
docker create --name vertcoind \
           -v /path/to/permanent/storage:/data \
           -p 5889:5889 \
           -p 5888:5888 \
           --network=host \
           --restart unless-stopped \
           -d firrae/vertcoind
```

Then, run your vertcoind instance and let it sync

```bash
docker start vertcoind
```

You can watch the progress with

```bash
docker logs vertcoind
```
Once done, you will need to build p2pool-vtc docker

```bash
git clone https://github.com/chadouming/p2pool-vtc
cd p2pool-vtc
docker build -t p2pool:latest .
```

Finally, you can run your p2pool node via docker !

Have a look at /path/to/permanent/storage/vertcoin.conf to get your rpc password then:

```bash
docker create --name p2pool_vtc \
           -e RPC_USER="rpc" \
           -e RPC_PASSWORD="thisisyourvertcoindrpcpassword" \
           -e VERTCOIND_HOST="127.0.0.1" \
           -e FEE="0.5" \
           -e FEE_ADDRESS="vtc1q6gzm0qw8hzfth632fxfzlmd4dj0ghy8762zxa4" \
           -e MAX_CONNECTIONS="100" \
           -v /path/to/permanent/storage/verthash.dat:/data/verthash.dat \
           --network=host \
           p2pool:latest
 ```
