from lfsr import lfsr

def stream_encrypt(text, polynomial):
    binary_text = ''.join(format(ord(letter), '08b') for letter in text)
    key_length = len(binary_text)
    encrypted_binary_text = ""
    encrypted_text = ""
    encrypted_letters = []
    key = lfsr(polynomial, key_length)
    #print(key)

    for count, digit in enumerate(binary_text):
        encrypted_binary_text += str(int(digit) ^ int(key[count]))

    #print(binary_text)
    #print(encrypted_binary_text)

    for i in range(0, len(encrypted_binary_text), 8):
        encrypted_letters.append(encrypted_binary_text[i:i + 8])
    encrypted_text = "".join([chr(int(letter, 2)) for letter in encrypted_letters])
    print(encrypted_text)
    return encrypted_text


def stream_decrypt(text, key):
    binary_text = ''.join(format(ord(letter), '08b') for letter in text)
    decrypted_binary_text = ""
    decrypted_text = ""
    decrypted_letters = []
    #print(key)
    for count, digit in enumerate(binary_text):
        decrypted_binary_text += str(int(digit) ^ int(key[count]))
    # print(binary_text)
    # print(encrypted_binary_text)

    for i in range(0, len(decrypted_binary_text), 8):
        decrypted_letters.append(decrypted_binary_text[i:i + 8])
    decrypted_text = "".join([chr(int(letter, 2)) for letter in decrypted_letters])
    print(decrypted_text)
    return decrypted_text


#stream_encrypt("DDDDD",5)