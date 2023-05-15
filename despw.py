"""9"""
def xor_bits(bit_array1, bit_array2):
    assert len(bit_array1) == len(bit_array2)
    result = []
    for i in range(len(bit_array1)):
        result.append(bit_array1[i] ^ bit_array2[i])
    return result

"""10"""
def split_to_6bits(text):
    result = []
    for i in range(8):
        chunk = text[i*6:i*6+6]
        result.append(chunk)
    return result

"""11"""
def get_sbox_index(b: str, i: int) -> int:
    row = int(b[0] + b[5], 2)
    col = int(b[1:5], 2)
    sbox_index = row * 16 + col
    return sbox_index

"""12"""
def s_box_transform(s_box_num, sbox_index):
    s_box = S_BOXES[s_box_num]
    return f'{s_box[sbox_index]:04b}'

def s_box_permutation(s_box_outputs):
    return ''.join(s_box_outputs)

def s_boxes_transformation(expanded_r_block):
    s_box_outputs = [s_box_transform(i, expanded_r_block[i*6:(i+1)*6]) for i in range(8)]
    return s_box_permutation(s_box_outputs)

"""13"""
def combine_blocks(blocks):
    combined = ''.join(blocks)
    return int(combined, 2)

"""14"""
def permutation_p(block):
    p_table = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]
    result = [0] * 32
    for i in range(32):
        result[i] = block[p_table[i] - 1]
    return result

"""15"""
def xor_blocks(block1, block2):
    result = [0] * len(block1)
    for i in range(len(block1)):
        result[i] = block1[i] ^ block2[i]
    return result

def calculate_rn(ln, rn_1, kn):
    expanded_rn_1 = expand_block(rn_1)
    xor_result = xor_blocks(expanded_rn_1, kn)
    s_result = s_block_substitution(xor_result)
    p_result = permutate_block(s_result)
    rn = xor_blocks(ln, p_result)
    return rn

"""16"""
L_n = R_n_1.copy()

"""17"""
def combine_blocks(R16, L16):
    return R16 + L16

"""18"""
# tablica permutacji IP-1
IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

def permute_IP_1(block):
    bits = list(block)
    permuted_bits = [bits[i-1] for i in IP_1]
    return ''.join(permuted_bits)
