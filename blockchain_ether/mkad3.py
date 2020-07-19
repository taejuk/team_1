from Crypto.PublicKey import ECC
from Crypto.Random import get_random_bytes
from web3 import Web3
from Crypto.Hash import keccak
from eth_keys import KeyAPI
from eth_keys.backends import NativeECCBackend

keys = KeyAPI(NativeECCBackend)


#private_key = ECC.generate(curve='secp256r1')
#public_key = private_key.public_key()
# print(private_key)
# print(public_key)
#public_keys = hex(private_key.pointQ.x)[2:]+hex(private_key.pointQ.y)[2:]
#keccak_hash = keccak.new(digest_bits=256)
# keccak_hash.update(public_keys.encode())
#full_address = keccak_hash.digest()
#address = full_address[-20:].hex()

a = ECC.EccPoint(67698366555394503456389735314747771212653231959194107680906447043311064147244, 18810034840740666198292649583024596625279737503538043214878145756695996563911,
                 curve="secp256r1").__mul__(83055155705272874845771629053143260293103953355863884734885738209571681001918)
public_x = hex(a.x)
public_y = hex(a.y)
public_keys = public_x[2:]+public_y[2:]
keccak_hash = keccak.new(digest_bits=256)
keccak_hash.update(public_keys.encode())
full_address = keccak_hash.digest()
address = full_address[-20:].hex()
print(address)
#private_keys = 개인키, address = 주소
