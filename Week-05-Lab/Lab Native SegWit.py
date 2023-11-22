# -*- coding: utf-8 -*-

'''
https://coinmarketcap.com/
https://www.coingecko.com/

tail -n 1 ~btc/snap/bitcoin-core/common/.bitcoin/debug.log
'''

# pip install bech32
# https://bitcoin.stackexchange.com/questions/91748/how-to-use-python-reference-for-encoding-a-bech32-address

import secrets
import hashlib
import bech32

# Generate a random private key
private_key = secrets.randbelow(2**256)

# Derive the corresponding public key
public_key = private_key.to_bytes(32, 'big')

# Compute the public key hash (hash160)
hash160 = hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()

# Create the native SegWit (P2WPKH) script
segwit_script = bytes([0x00, len(hash160)]) + hash160

# Encode the native SegWit (P2WPKH) address
hrp = "bc"  # Human-readable part for mainnet SegWit
version = segwit_script[0]
witprog = segwit_script[2:]  # Exclude the leading 0x00 and length byte
address = bech32.encode(hrp, version, witprog)

print("Private Key:", private_key)
print("Native SegWit (P2WPKH) Address:", address)
