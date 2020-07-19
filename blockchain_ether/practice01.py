from web3 import Web3
import sss
# endpoint -실험하는 곳
infura_url = "https://ropsten.infura.io/v3/18584ab189e842369a1c2e2a257791a3"

web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
account_1 = '0x7Efb9447e3903eF7FC89F807984b44BACa29d3b7'
account_2 = '0x81b7E08F65Bdf5648606c89998A9CC8164397647'
private_key = 'E86B4ED9A1510D5D5E532A02FEFE4F3117DB9576A9CB3060820EE58FB175F1DD'
key = []

for i in range(0, 64, 4):
    key.append(private_key[i:i+4])

recon = ""
for i in key:
    recon += "{0:x}".format(sss.start(3, 5, int(i, 16)))
recon = recon.upper()
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
print(private_key)
print(recon)
#signed_tx = web3.eth.account.signTransaction(tx, recon)

#tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
