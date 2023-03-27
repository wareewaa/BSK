from railfence import rail_fence_encrypt, rail_fence_decrypt
from cezar import caesar_cipher_encrypt, caesar_cipher_decrypt
from vigenere import vigenere_cipher_encrypt, vigenere_cipher_decrypt


def encrypt(text, key, mode):
    if mode == 1:
        print("1")
        encryptedText = rail_fence_encrypt(text, key)
    elif mode == 2:
        print("1")
    elif mode == 3:
        print("1")
    elif mode == 4:
        print("1")
    elif mode == 5:
        print("1")
        encryptedText = caesar_cipher_encrypt(text, key)
    elif mode == 6:
        print("1")
        encryptedText = vigenere_cipher_encrypt(text, key)
    return encryptedText


def decrypt(text, key, mode):
    if mode == 1:
        print("2")
        decryptedText = rail_fence_decrypt(text, key)
    elif mode == 2:
        print("2")
    elif mode == 3:
        print("2")
    elif mode == 4:
        print("2")
    elif mode == 5:
        print("2")
        decryptedText = caesar_cipher_decrypt(text, key)
    elif mode == 6:
        print("2")
        decryptedText = vigenere_cipher_decrypt(text, key)
    return decryptedText
