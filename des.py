text = "12345678"
key = "1100010010001010010101100100101101110000011000111111000111100111"
ip_tuple = (58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7)

pc_tuple = (57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4)

pc2_tuple = (14, 17, 11, 24, 1, 5,
             3, 28, 15, 6, 21, 10,
             23, 19, 12, 4, 26, 8,
             16, 7, 27, 20, 13, 2,
             41, 52, 31, 37, 47, 55,
             30, 40, 51, 45, 33, 48,
             44, 49, 39, 56, 34, 53,
             46, 42, 50, 36, 29, 32)

shift_tuple = (1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1)

e_tuple = (32, 1, 2, 3, 4, 5,
           4, 5, 6, 7, 8, 9,
           8, 9, 10, 11, 12, 13,
           12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21,
           20, 21, 22, 23, 24, 25,
           24, 25, 26, 27, 28, 29,
           28, 29, 30, 31, 32, 1)

def transform_binary(text):
    binary_text = ''.join(format(ord(letter), '08b') for letter in text)
    binary_text_list = [bit for bit in binary_text]
    #print(binary_text)
    #print(binary_text_list)
    permutated_block = permutation(binary_text_list, ip_tuple)
    LR = split(permutated_block)
    expanded_block = block_expand(LR[1])

def permutation(block, permutation):
    permutated_block = []
    for count, bit in enumerate(permutation):
        temp = permutation[count] - 1
        permutated_block.append(block[temp])
    return permutated_block




def split(table):
    middle_index = int(len(table)/2)
    blockL = table[:middle_index]
    blockR = table[middle_index:]
    LR = (blockL, blockR)
    return LR


def key_reduction(key):
    new_key = permutation(key, pc_tuple) #key in list
    s = ''.join(str(x) for x in new_key) #key in string
    key_split(new_key)
    return new_key

def key_split(key):
    LR = split(key)
    keyL = LR[0]
    keyR = LR[1]
    print(LR)


def key_shift(keyLR, iteration): #step 6 and 7
    L = keyLR[0]
    R = keyLR[1]
    for n in range(shift_tuple[iteration]):
        L.append(L.pop(0))
        R.append(R.pop(0))
    key = L + R
    new_key = permutation(key, pc2_tuple)


def block_expand(block):
    expanded_block = permutation(block, e_tuple)
    return expanded_block

#transform_binary(text)
#print(ip_tuple)
#table_split(key)
key_reduction(key)