from p2pool.bitcoin import networks

PARENT=networks.nets['vertcoin']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=12 # blocks
IDENTIFIER='a06e81c82fcaff83'.decode('hex')
PREFIX='7c3814b6ccdcf984'.decode('hex')
P2P_PORT=9347
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=9181
BOOTSTRAP_ADDRS='vtc2.alwayshashing.com pool.vtconline.org uk1.vtconline.org pool.boxienet.net'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-vtc'
VERSION_CHECK=lambda v: True
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16
