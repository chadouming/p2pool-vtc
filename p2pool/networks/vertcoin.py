from p2pool.bitcoin import networks

PARENT=networks.nets['vertcoin']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=12 # blocks
IDENTIFIER='a06a81c827cab983'.decode('hex')
PREFIX='7c3614a6bcdcf784'.decode('hex')
P2P_PORT=9346
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=9171
BOOTSTRAP_ADDRS='vtc.alwayshashing.com crypto.office-on-the.net pool.vtconline.org p2pool.kosmoplovci.org uk1.vtconline.org pool.boxienet.net'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-vtc'
VERSION_CHECK=lambda v: True
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16
