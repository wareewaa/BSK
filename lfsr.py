import random


def lfsr(polynomial, key_length):
    result = []
    string = format(random.getrandbits(polynomial), '0' +str(polynomial) +'b')
    array = [digit for digit in string]
    #print (array)
    def shift(array):
        n = len(array)
        result.append(array[n-1])
        print(array[n-1])
        new = int(array[n-1]) ^ int(array[0])
        for i in range(n-1, 0, -1):
            array[i] = array[i-1]
        array[0] = new

    i = 0
    while i < key_length or key_length == 0:
        shift(array)
        i += 1
    print("".join(str(bit) for bit in result))
    return result


lfsr(8, 5)