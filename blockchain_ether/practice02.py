from web3 import Web3
'''
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
'''
infura_url = "https://mainnet.infura.io/v3/18584ab189e842369a1c2e2a257791a3"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

account_1 = "0xB0426a941CCE64d205814c9B8c2d9ab1bDdA31d6"
account_2 = "0xC2122aa2E494C3E3c5b4e13ad249798B5D891761"

'''
private_key = "40b818c37cd37e740a482b4f3ab3e1ea4fe71117b9bcc740d618ac54f3dbc30c"
# get the nonce
nonce = web3.eth.getTransactionCount(account_1)
print(nonce)
# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)

'''
