# pip install cryptography
# C:\Python\Python311\Lib\site-packages\cryptography
# %appdata%
# C:\Users\dkkim\AppData\Local\Programs\Python\<Python Version>\Lib\site-packages\cryptography

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

import base64
import binascii

def rsa_key_generation(bits=1024):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=bits
    )
    return private_key

def rsa_encrypt(public_key, plaintext):
    ciphertext = public_key.encrypt(
        plaintext.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def rsa_decrypt(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode('utf-8')

def serialize_key(key):
    key_bytes = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    return base64.b64encode(key_bytes).decode('utf-8')

def main():
    private_key = rsa_key_generation()
    public_key = private_key.public_key()

#   print("Private key :", private_key)
#   print("Public key :", public_key)

    private_key_str = serialize_key(private_key)
    print("Private key :")
    print(private_key_str)

    public_key_str = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
    print("Public key :")
    print(public_key_str)

#   plaintext = "Hello, RSA 1024-bit!"
    plaintext = input("Enter Data : ")
    print("Original :", plaintext)
#   print("Data : ", plaintext)

    ciphertext = rsa_encrypt(public_key, plaintext)
    ciphertext_hex = binascii.hexlify(ciphertext).decode()
    print("Ciphertext (in Hex) :")
    print(ciphertext_hex)

    print("Encrypted :")
    print(ciphertext)

    decrypted_text = rsa_decrypt(private_key, ciphertext)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
