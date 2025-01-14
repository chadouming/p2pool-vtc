import os
import platform
import hashlib

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

import verthash

verthash_data = None
if verthash_data is None:
    with open('verthash.dat', 'rb') as f:
        verthash_data = f.read()

    verthash_sum = hashlib.sha256(verthash_data).hexdigest().encode('ascii')
    assert verthash_sum == b'a55531e843cd56b010114aaf6325b0d529ecf88f8ad47639b6ededafd721aa48'

def verthash_hash(dat):
    return verthash.getPoWHash(dat, verthash_data)

P2P_PREFIX = bytes.fromhex('fabfb5da') # new net magic
P2P_PORT = 5889
ADDRESS_VERSION = 71
ADDRESS_P2SH_VERSION = 5
HUMAN_READABLE_PART = b'vtc'
RPC_PORT = 5888
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_block_header(bitcoind, '4d96a915f49d40b1e5c2844d1ee2dccb90013a990ccea12c492d22110489f0c4')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(verthash_hash(data))
BLOCK_PERIOD = 150 # s
SYMBOL='VTC'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Vertcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Vertcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.vertcoin'), 'vertcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/vtc/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/vtc/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/vtc/tx.dws?'
SANE_TARGET_RANGE =  (2**256//100000000000000000 - 1,  2**256//100000 - 1)
DUMB_SCRYPT_DIFF = 256
DUST_THRESHOLD = 0.001e8
