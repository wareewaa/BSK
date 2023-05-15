text = "12345678"

ip_tuple = (58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7)


def transform_binary(text):
    binary_text = ''.join(format(ord(letter), '08b') for letter in text)
    binary_text_list = [bit for bit in binary_text]
    #print(binary_text)
    #print(binary_text_list)
    initial_permutation(binary_text_list)


def initial_permutation(block):
    #print("essa")
    permutated_block = []
    for count, bit in enumerate(block):
        #temp = block[count]
        temp = ip_tuple[count] - 1
        #print(str(temp) + "    " + str(count))
        permutated_block.append(block[temp])
    #print(permutated_block)
    #print(block[53])

transform_binary(text)
#print(ip_tuple)