def caesar_cipher_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 + int(key)) % 26 + 97)
            ciphertext += shifted_char.upper() if char.isupper() else shifted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 - int(key)) % 26 + 97)
            plaintext += shifted_char.upper() if char.isupper() else shifted_char
        else:
            plaintext += char
    return plaintext
