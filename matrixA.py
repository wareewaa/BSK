def matrix_a_encrypt(text, key):
    cols = len(key)
    rows = int(len(text)/cols) + 1
    encryptedText = ""
    for row in range(0, rows):
        for number in key:
            index = int(number) + row * cols - 1
            if index < len(text):
                encryptedText += text[index]
    return encryptedText


def matrix_a_decrypt(text, key):
    cols = len(key)
    rows = int(len(text) / cols) + 1
    decryptedText = ""
    count_index = 0
    for row in range(0, rows):
        fragment = ['', '', '', '']
        for count, number in enumerate(key):
            number_index = int(number) + row * cols - 1
            if number_index >= len(text):
                count_index -= 1
            elif count_index < len(text):
                fragment[int(number)-1] = text[count_index]
            count_index += 1
        decryptedText += ''.join(fragment)
    return decryptedText


