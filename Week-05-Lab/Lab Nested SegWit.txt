# -*- coding: utf-8 -*-

import hashlib
import binascii
import base58
import os
from ecdsa import SigningKey, SECP256k1

# Generate a random private key
private_key = binascii.hexlify(os.urandom(32)).decode()

# Derive the corresponding public key (compressed)
sk = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1)
vk = sk.get_verifying_key()
public_key_compressed = binascii.hexlify(vk.to_string("compressed")).decode()

# Compute the public key hash (hash160)
public_key_bytes = bytes.fromhex(public_key_compressed)
hash160 = hashlib.new('ripemd160', hashlib.sha256(public_key_bytes).digest()).digest()

# Create the P2WPKH (SegWit) script
segwit_script = bytes([0x00, len(hash160)]) + hash160

# Compute the script hash (SHA256 of segwit_script)
script_hash = hashlib.sha256(segwit_script).digest()

# Add the network prefix (0x05 for mainnet, 0xC4 for testnet)
network_prefix = b'\x05'  # Mainnet, change to b'\xC4' for Testnet

# Create the P2SH-P2WPKH (Nested SegWit) address
p2sh_p2wpkh_address_bytes = network_prefix + script_hash
checksum = hashlib.sha256(hashlib.sha256(p2sh_p2wpkh_address_bytes).digest()).digest()[:4]
p2sh_p2wpkh_address_bytes += checksum
p2sh_p2wpkh_address = base58.b58encode(p2sh_p2wpkh_address_bytes).decode()

print("Private Key:", private_key)
print("P2SH-P2WPKH (Nested SegWit) Address:", p2sh_p2wpkh_address)
print("Public Key (Compressed):", public_key_compressed)
