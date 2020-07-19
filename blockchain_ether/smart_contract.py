from web3 import Web3

# ganache랑 연결하기
ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0xe096981A7C81623B653178493D000B69602F3a39"
account_2 = "0x70b7807734E107e2606a8CD40e3bBf8E68f2Da7B"

private_key = "b1754452a45c1e6cf1834c705e2508d9db316a6dfd0463079f89fcd221bc9d68"

nonce = web3.eth.getTransactionCount(account_1)  # nonce 받기

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)
