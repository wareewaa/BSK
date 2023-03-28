def matrix_c_encrypt(text, key):
    order = get_order(key)
    print(order)
    encryptedText = ''
    text = text.replace(" ", "")
    newText = [str(0)] * len(key) * len(key)
    letter_count = 0
    for i in range(0, len(order)):
        index = 0 + len(key) * i
        for n in range(0, order[i] + 1):
            newText[index] = text[letter_count]
            letter_count += 1
            index += 1
            if letter_count >= len(text):
                break
        if letter_count >= len(text):
            break
    for element in order:
        index = element
        while index < len(newText):
            encryptedText += newText[index]
            index += len(key)
        encryptedText += " "
    encryptedText = encryptedText.replace("0", "")[:-1]
    print(encryptedText)
    return encryptedText



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




