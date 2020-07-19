from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins, HdWalletWordsNum
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from web3 import Web3
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify
import ssss
# hd_wallet 생성
hd_wallet_fact = HdWalletFactory(HdWalletCoins.ETHEREUM)
hd_wallet = hd_wallet_fact.CreateRandom(
    "eth_wallet", HdWalletWordsNum.WORDS_NUM_24)
hd_wallet.Generate(addr_num=3)
dicts = hd_wallet.ToDict()

# sss 적용해서 ether 전송하기
# 1 설정
infura_url = "https://ropsten.infura.io/v3/18584ab189e842369a1c2e2a257791a3"
web3 = Web3(Web3.HTTPProvider(infura_url))

# 2 주소 및 개인키 설정
addr = dicts["addresses"]["address_1"]["address"]
private_keyes = dicts["addresses"]["address_1"]["raw_priv"]
private_key = bytes.fromhex(dicts["addresses"]["address_1"]["raw_priv"])
account_1 = addr
account_2 = '0x81b7E08F65Bdf5648606c89998A9CC8164397647'
account_1 = web3.toChecksumAddress(account_1)
nonce = web3.eth.getTransactionCount(account_1)


# 트랜잭션 설정
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
signed_tx = web3.eth.account.signTransaction(
    tx, recon.hex())  # 트랜잭션에 서명을 할 때, 변수 값으로 개인키와 트래
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
