from pywalletmaster.pywallet import wallet
from pywallet import walley
from Crypto.Hash import keccak
from eth_keys import keys
from eth_keys import KeyAPI
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from web3 import Web3
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify
import ssss

# create hd wallet
# seed = wallet.generate_mnemonic()  # generate mnemonic code words

seed = "opinion kingdom unveil loyal special side notable tone simple laugh again reunion"
w = wallet.create_wallet(network="ETH", seed=seed,
                         children=1)  # create wallet
