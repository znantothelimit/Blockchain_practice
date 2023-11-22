"""
651050 th block
https://www.blockchain.com/btc/address/1ALFvaFzgM6KkRBqZRGwEg14amaF8pz97o

https://www.blockchain.com/explorer/api/blockchain_api
* Unspent Outputs => https://blockchain.info/unspent?active=$address

https://www.blockchain.com/explorer
* Developers => https://www.blockchain.com/explorer/api

What is a Satoshi ?
1 BTC = 100,000,000 Satoshi = 10^8 Satoshi
Satoshi is the smallest unit of Bitcoin

"""

import requests

addr = "bc1quhruqrghgcca950rvhtrg7cpd7u8k6svpzgzmrjy8xyukacl5lkq0r8l2d"
bcURL = "https://blockchain.info/unspent?active=" + addr
res = requests.get(url=bcURL)

# res
# res.status_code
if res.status_code != 200:
	print("\n", res.text)
else:
	data = res.json()
#	data
	utxo = data['unspent_outputs']
#	utxo
	totalBalance = 0
	print('\nNumber of UTXO = ', len(utxo))
	for n in range(len(utxo)):
		print("***** UTXO =", n)
		print("Confirmations =", utxo[n]['confirmations'])
		print("tx_hash =", utxo[n]['tx_hash'])
		print("tx_output_n =", utxo[n]['tx_output_n'])
		print("value =", utxo[n]['value'])
		print()
		totalBalance += utxo[n]['value']

	print("\nTotal Balance =", totalBalance, '(Satoshi)')
