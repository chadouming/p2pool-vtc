from p2pool.bitcoin import networks

PARENT=networks.nets['vertcoin']
SHARE_PERIOD=10 # seconds
CHAIN_LENGTH=(7*24*60*60)//SHARE_PERIOD # shares
REAL_CHAIN_LENGTH=(7*24*60*60)//SHARE_PERIOD # shares
TARGET_LOOKBEHIND=30 # shares
SPREAD=12 # blocks
IDENTIFIER='a07e81d83ddafd83'.decode('hex')
PREFIX='7c3814fffcdcf988'.decode('hex')
P2P_PORT=9348
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=9191
BOOTSTRAP_ADDRS='uscentral1.vtconline.org'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-vtc'
VERSION_CHECK=lambda v: True
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16
