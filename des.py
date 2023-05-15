text = "Q³^xªBQ³^xªBHeÌ±¥Ø"
key = "0001001100110100010101110111100110011011101111001101111111110001"
type = 'dsa'


ip_tuple = (58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7)

reverse_ip_tuple = (40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25)

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

p_tuple = (16, 7, 20, 21,
           29, 12, 28, 17,
           1, 15, 23, 26,
           5, 18, 31, 10,
           2, 8, 24, 14,
           32, 27, 3, 9,
           19, 13, 30, 6,
           22, 11, 4, 25)

S_BOXES = [
    (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13),

    (15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9),

    (10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12),

    (7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14),

    (2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3),

    (12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13),

    (4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12),

    (13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11)]


def des_encryption(text, key, decrypt):
    bin_text = transform_binary(text)
    binary_text = ''
    bit_amount = len(bin_text)
    missing_bits = 0

    if bit_amount % 64 == 0:
        for n in range(int(bit_amount / 64)):
            binary_text += des_1block_encryption(bin_text[n*64:n*64+64], key, decrypt)
    else:
        missing_bits = 64 - (bit_amount % 64)
        #print(missing_bits)
        for bit in range(missing_bits):
            #print(bit)
            bin_text.append('0')
            #print(bin_text)
        for n in range(int(bit_amount / 64) + 1):
            binary_text += des_1block_encryption(bin_text[n*64:n*64+64], key, decrypt)

    print(missing_bits)
    print(binary_text)
    #if missing_bits > 0:
    #    binary_text = binary_text[:-missing_bits]
    print("XD")
    print(binary_text)
    print("XD")


    #decBlock = int(binary_text, 2)
    #decrypted_letters = []
    binary_chunks = [binary_text[i:i + 8] for i in range(0, len(binary_text), 8)]
    decoded_text = ''.join(chr(int(chunk, 2)) for chunk in binary_chunks)
    print("Decoded text:", decoded_text)
    return decoded_text

def des_1block_encryption(text, key, decrypt):
    block = text  # step1
    block = permutation(block, ip_tuple)  # step2
    LR = split(block)  # step3
    R = LR[1]
    L = LR[0]
    reduced_key = key_reduction(key)  # step4
    CD = split(reduced_key)  # step5
    C = []
    D = []
    K = []
    C.append(CD[0])
    D.append(CD[1])
    for n in range(16):  # step6
        key_shift_result = key_shift(C[n], D[n], n)
        C.append(key_shift_result[0])
        D.append(key_shift_result[1])
        CnDn = key_shift_result[0] + key_shift_result[1]  # step7
        K.append(permutation(CnDn, pc2_tuple))

    for n in range(16):
        newR = block_expand(R)  # step8
        if decrypt == True:
            newR = xor_blocks(newR, K[15-n])  # step9
        else:
            newR = xor_blocks(newR, K[n])  # step9
        newR = ''.join(str(x) for x in newR)
        split_block = split_to_6bits(newR)  # step10
        new_block = []
        for count, chunk in enumerate(split_block):
            sbox_index = get_sbox_index(chunk)  # step11
            sbox_value = s_box_transform(count, sbox_index)  # step12
            new_block.append(sbox_value)
        new_block = combine_blocks(new_block)  # step13
        # print(new_block)
        new_block = permutation(new_block, p_tuple)  # step14
        newR = xor_blocks(new_block, L)
        L = R
        R = newR
        # print(''.join(str(x) for x in L))
        # print(''.join(str(x) for x in R))
    #print(R)
    #print(L)
    block = R + L
    block = permutation(block, reverse_ip_tuple)
    #print(block)
    binaryBlock = ''.join(str(x) for x in block)
    #print(binaryBlock)
    return binaryBlock



def get_sbox_index(b: str) -> int:
    row = int(b[0] + b[5], 2)
    col = int(b[1:5], 2)
    sbox_index = row * 16 + col
    return sbox_index


def transform_binary(text):
    if type == 'binary':
        binary_text_list = [bit for bit in text]
        result = binary_text_list
    else:
        binary_text = ''.join(format(ord(letter), '08b') for letter in text)
        binary_text_list = [bit for bit in binary_text]
        result = binary_text_list
    return result


def permutation(block, permutation):
    permutated_block = []
    for count, bit in enumerate(permutation):
        temp = permutation[count] - 1
        permutated_block.append(block[temp])
    return permutated_block


def split(table):
    middle_index = int(len(table) / 2)
    blockL = table[:middle_index]
    blockR = table[middle_index:]
    LR = (blockL, blockR)
    return LR



def key_reduction(key):
    new_key = permutation(key, pc_tuple)  # key in list
    # new_key = ''.join(str(x) for x in new_key)  # key in string
    return new_key


def key_shift(Cn, Dn, iteration):  # step 6 and 7
    for n in range(shift_tuple[iteration]):
        Cn.append(Cn.pop(0))
        Dn.append(Dn.pop(0))
    key_shifted = (Cn, Dn)
    # joinC = ''.join(Cn)
    # joinD = ''.join(Dn)
    # joinKey = (joinC, joinD)
    # print(joinKey)
    return key_shifted
    # new_key = permutation(key, pc2_tuple)


def block_expand(block):
    expanded_block = permutation(block, e_tuple)
    return expanded_block


def split_to_6bits(text):
    result = []
    for i in range(8):
        chunk = text[i * 6:i * 6 + 6]
        result.append(chunk)

    return result


def s_box_transform(s_box_num, sbox_index):
    s_box = S_BOXES[s_box_num]
    return f'{s_box[sbox_index]:04b}'



def combine_blocks(blocks):
    combined = ''.join(blocks)
    return combined



def xor_blocks(block1, block2):
    result = []
    for i in range(len(block1)):
        result.append(int(block1[i]) ^ int(block2[i]))
    return result

#des_1block_encryption(text, key, True)
des_encryption(text,key,True)