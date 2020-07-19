from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from web3 import Web3
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify
import ssss

# 주소 생성
'''
private_key = keccak_256(token_bytes(32)).digest()  # 고정 길이 해시값
public_key = PublicKey.from_valid_secret(
    private_key).format(compressed=False)[1:]
addr = keccak_256(public_key).digest()[-20:]
addr = '0x'+addr.hex()
#주소 및 개인키 저장
with open("adr.txt", "w") as f:
    f.write(addr)
with open("private_key.pem", 'wb') as f:
    f.write(private_key)
'''

# 주소 및 개인키 읽어오기
with open("adr.txt", "r") as f:
    addr = f.read()
with open("private_key.pem", "rb") as f:
    private_key = f.read()

infura_url = "https://ropsten.infura.io/v3/18584ab189e842369a1c2e2a257791a3"

web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
account_1 = addr
account_2 = '0x81b7E08F65Bdf5648606c89998A9CC8164397647'
account_1 = web3.toChecksumAddress(account_1)
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
# sign transaction
# sss 사용하기
shares = ssss.split(private_key, 5, 3)
recon = ssss.combine(3, shares)
signed_tx = web3.eth.account.signTransaction(tx, recon.hex())
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
