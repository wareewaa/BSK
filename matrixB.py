def matrix_b_encrypt(text, key):
    order = get_order(key)
    print(order)
    text = text.replace(" ", "")
    encryptedText = ''
    cols = len(key)

    for col in range(0, cols):
        index = order[col]
        while index < len(text):
            encryptedText += text[index]
            index += cols
        encryptedText += " "
    return encryptedText[:-1]


def matrix_b_decrypt(text, key):
    order = get_order(key)
    print(order)
    decryptedText = [str(0)] * len(text)
    cols = len(key)
    word_count = 0
    index = order[word_count]
    for letter in text:
        if letter == ' ':
            word_count += 1
            index = order[word_count]
        else:
            decryptedText[index] = letter
            index += cols
    decryptedText = ''.join(decryptedText).replace("0", "")
    return decryptedText


def get_order(key):
    sorted_key = sorted(key.upper())
    order_key = list(key)
    count = 0
    order = []
    for element in sorted_key:
        order_key[order_key.index(element)] = count
        count += 1
    for x in range(len(key)):
        order.append(order_key.index(x))
    return order


