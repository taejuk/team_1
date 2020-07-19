from eth_keys import keys
from eth_keys import KeyAPI
from eth_keys.backends import NativeECCBackend
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from web3 import Web3
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify

private_key = keccak_256(token_bytes(32)).digest()
pk = keys.PrivateKey(private_key)
print(pk)
print(pk.public_key.to_address())
