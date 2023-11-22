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