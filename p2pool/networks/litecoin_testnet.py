from p2pool.bitcoin import networks

PARENT = networks.nets['litecoin_testnet']
SHARE_PERIOD = 4 # seconds
CHAIN_LENGTH = 20*60//3 # shares
REAL_CHAIN_LENGTH = 20*60//3 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = bytes.fromhex('cca5e24ec6408b1e')
PREFIX = bytes.fromhex('ad9614f6466a39cf')
P2P_PORT = 19338
MIN_TARGET = 0
MAX_TARGET = 2**256//20 - 1
PERSIST = False
WORKER_PORT = 19327
BOOTSTRAP_ADDRS = 'forre.st'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
