def rail_fence_encrypt(plaintext, key):
    fence = [[] for _ in range(int(key))]
    rail = 0
    direction = 1
    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        if rail == int(key) - 1 or rail == 0:
            direction = -direction
    ciphertext = ''.join([''.join(row) for row in fence])
    return ciphertext

def rail_fence_decrypt(ciphertext, key):
    fence = [[] for _ in range(int(key))]
    rails = list(range(int(key)))
    rail = 0
    direction = 1
    for char in ciphertext:
        fence[rail].append(None)
        rail += direction
        if rail == int(key) - 1 or rail == 0:
            direction = -direction
    index = 0
    for rail in rails:
        for i in range(len(fence[rail])):
            if fence[rail][i] is None:
                fence[rail][i] = ciphertext[index]
                index += 1
    rail = 0
    direction = 1
    plaintext = ''
    for _ in range(len(ciphertext)):
        plaintext += fence[rail].pop(0)
        rail += direction
        if rail == int(key) - 1 or rail == 0:
            direction = -direction
    plaintext = plaintext.replace('-', '')
    return plaintext