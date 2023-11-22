# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

import binascii

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return cipher.iv + ciphertext

def aes_decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return decrypted_data.decode('utf-8')

def main():
    key = get_random_bytes(16)  # 128-bit key (16 bytes)

    plaintext = input("Enter Data : ")
    print("Original :", plaintext)

    ciphertext = aes_encrypt(key, plaintext)
    print("Encrypted :")
    print(ciphertext)

    ciphertext_hex = binascii.hexlify(ciphertext).decode()
    print("Ciphertext (in Hex) :")
    print(ciphertext_hex)

    decrypted_data = aes_decrypt(key, ciphertext)
    print("Decrypted :", decrypted_data)

if __name__ == "__main__":
    main()
