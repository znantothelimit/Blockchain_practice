**********************************************************************************************************
* Lab 1: Generate Legacy Bitcoin Address by ECDSA

c:\...> pip install ecdsa
c:\...> pip install base58
c:\...> python

import hashlib
import ecdsa
import base58

def generate_bitAddr():
    # Generate Private Key
    priv = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    priv_hex = priv.to_string().hex()

    # Generate Public Key
    pub = priv.get_verifying_key()
    pub_bytes = pub.to_string()

    # SHA256 (PublicKey)
    sha256_hash = hashlib.sha256(pub_bytes).digest()

    # RIPEMD160 Hash
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

    # Version Byte(0x00) + Hash160 => Checksum
    payload = b'\x00' + ripemd160_hash
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    addrBytes = payload + checksum

    # Base58Check Encoding
    bitAddr = base58.b58encode(addrBytes).decode()

    return bitAddr

# Create Legacy Bitcoin Address
bitAddr = generate_bitAddr()
print('Bitcoin Address:', bitAddr)

**********************************************************************************************************

c:\...> pip install cryptos
c:\...> python

**********************************************************************************************************
* Lab 2 : Legacy Address

from cryptos import *

# priv = random_key()

priv = sha256("xx")
pub = privtopub(priv)
bitaddr = pubtoaddr(pub)

14zN981AqUVfgfCbFF2tXWAm57XfXvQXe2

**********************************************************************************************************
* Lab 3 : Legacy Address

from cryptos import *

// priv = random_key()
priv = sha256('dkkim')
pub = privkey_to_pubkey(priv)
pub
addr = pubkey_to_address(pub)

"173HjbiTQfbu8yqscfGdZQE7VY9QpdG1Ev"

**********************************************************************************************************
* Lab 4 : Nested SegWit Address

from cryptos import *

// priv = sha256('dkkim')
priv = random_key()

b = Bitcoin()
toAddr = b.privtop2wpkh_p2sh(priv)	// 3Mrcg1xUtTFbpYTzjodry9KJ8t1465rnPU

**********************************************************************************************************
* Lab 5 : Send Tx

// SegWit addr for transfer
// https://mempool.space/tx/f5cd50ab5e42286966e2f6cd46b84d54109c5a491a4aa5aeab2afa229c4e14e6

fromAddr = "bc1quhruqrghgcca950rvhtrg7cpd7u8k6svpzgzmrjy8xyukacl5lkq0r8l2d"

// get UTXO from SegWit addr
inputs = b.unspent(fromAddr)

// set SegWit field for UTXO to use
inputs[0]['segwit'] = True

// balance = sum(i['value'] for i in inputs)
balance= inputs[0]['value']
fee = 200

// Define Output in Tx
outs = [{'value': balance - fee, 'address': toAddr}]

// Create Tx
tx = b.mktx(inputs,  outs)

// add Signature
signed = b.signall(tx, priv)

// transfer Tx to Mempool
b.pushtx(signed)

// Error : (Script failed an OP_EQUALVERIFY operation)

**********************************************************************************************************
