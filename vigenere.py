def vigenere_cipher_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 + (ord(key[key_index % len(key)].lower()) - 97)) % 26 + 97)
            ciphertext += shifted_char.upper() if char.isupper() else shifted_char
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_cipher_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 - (ord(key[key_index % len(key)].lower()) - 97)) % 26 + 97)
            plaintext += shifted_char.upper() if char.isupper() else shifted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext