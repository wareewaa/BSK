from railfence import rail_fence_encrypt, rail_fence_decrypt
from cezar import caesar_cipher_encrypt, caesar_cipher_decrypt
from vigenere import vigenere_cipher_encrypt, vigenere_cipher_decrypt
from matrixA import matrix_a_encrypt, matrix_a_decrypt
from matrixB import matrix_b_encrypt, matrix_b_decrypt
from matrixC import matrix_c_encrypt # matrix_c_decrypt
from des import des_1block_encryption


def encrypt(text, key, mode):
    if mode == 1:
        encryptedText = rail_fence_encrypt(text, key)
    elif mode == 2:
        encryptedText = matrix_a_encrypt(text, key)
    elif mode == 3:
        encryptedText = matrix_b_encrypt(text, key)
    elif mode == 4:
        encryptedText = matrix_c_encrypt(text, key)
    elif mode == 5:
        encryptedText = caesar_cipher_encrypt(text, key)
    elif mode == 6:
        encryptedText = vigenere_cipher_encrypt(text, key)
    elif mode == 7:
        encryptedText = des_1block_encryption(text, key, False)
    return encryptedText


def decrypt(text, key, mode):
    if mode == 1:
        decryptedText = rail_fence_decrypt(text, key)
    elif mode == 2:
        decryptedText = matrix_a_decrypt(text, key)
    elif mode == 3:
        decryptedText = matrix_b_decrypt(text, key)
    elif mode == 4:
        decryptedText = " ... "
    elif mode == 5:
        decryptedText = caesar_cipher_decrypt(text, key)
    elif mode == 6:
        decryptedText = vigenere_cipher_decrypt(text, key)
    elif mode == 7:
        decryptedText = des_1block_encryption(text, key, True)
    return decryptedText
