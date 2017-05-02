from p2pool.bitcoin import networks

PARENT=networks.nets['vertcoin_testnet']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=12 # blocks
IDENTIFIER='a06a81c827cab972'.decode('hex')
PREFIX='7c3614a6bcdcf793'.decode('hex')
P2P_PORT=9345
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=9175
BOOTSTRAP_ADDRS='fr1.vtconline.org'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-vtc-testnet'
VERSION_CHECK=lambda v: True
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16
