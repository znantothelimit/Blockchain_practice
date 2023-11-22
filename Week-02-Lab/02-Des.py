# pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

import binascii

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), DES.block_size))
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_data.decode('utf-8')

def main():
    key = get_random_bytes(8)  # 64-bit key (8 bytes)
    plaintext = input("Enter Data : ")
    print("Original :", plaintext)

    ciphertext = des_encrypt(key, plaintext)
    print("Encrypted :")
    print(ciphertext)

    ciphertext_hex = binascii.hexlify(ciphertext).decode()
    print("Ciphertext (in Hex) :")
    print(ciphertext_hex)

    decrypted_data = des_decrypt(key, ciphertext)
    print("Decrypted:", decrypted_data)

if __name__ == "__main__":
    main()
