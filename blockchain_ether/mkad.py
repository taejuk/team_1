from Crypto.Hash import keccak
import binascii
import ecdsa
from ecdsa import SigningKey, VerifyingKey
from web3 import Web3
import sss
# endpoint -실험하는 곳
infura_url = "https://ropsten.infura.io/v3/18584ab189e842369a1c2e2a257791a3"

web3 = Web3(Web3.HTTPProvider(infura_url))
#keccak_hash = keccak.new(data=b'kimtaeju', digest_bits=256).digest()
# private_key = (binascii.hexlify(keccak_hash))  # 개인키 생성
# 개인키 공개키 생성
# 0x348ce564d427a3311b6536bbcff9390d69395b06ed6c486954e971d960fe8709
'''
primary_key = SigningKey.generate()
public_key = primary_key.get_verifying_key()

open("private.txt", "wb").write(primary_key.to_string())
open("public.txt", "wb").write(public_key.to_string())
'''
sk = SigningKey.from_pem(open("private.pem").read())
pk = VerifyingKey.from_pem(open("public.pem").read())

'''
keccak_hash = keccak.new(data=bytes(pk.to_string()), digest_bits=256).digest()
address = (binascii.hexlify(keccak_hash))[-21:-1]
print(address)

# print(wallet)
'''
