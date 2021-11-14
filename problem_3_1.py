# Author: Erlend Siqveland

import heapq
import random
from heapq import heappop, heappush

length_of_string = 0

norwegian_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']


def is_leaf(root):
    return root.left is None and root.right is None


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def encode(root, string, huffman_code):
    if root is None:
        return

    # found a leaf node
    if is_leaf(root):
        huffman_code[root.ch] = string if len(string) > 0 else '1'

    encode(root.left, string + '0', huffman_code)
    encode(root.right, string + '1', huffman_code)


# Generate a string using our norwegian alphabet
def generate_string(length):
    string = ''.join((random.choice(norwegian_alphabet) for x in range(length)))
    return string


# Get the ascii value of our letter
def to_ascii(letter):
    ascii_number = ord(letter)
    return ascii_number


# Go through our string and count frequency of each letter
def calculate_frequency(string):
    frequencies = dict()
    for letter in string:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    return frequencies


def fixed_length(item):
    a = str(item)
    a = a.rjust(4, '0')
    return a


def huffman(string):
    if len(string) == 0:
        return
    else:
        freq = calculate_frequency(string)

        prioirty = [Node(k, v) for k, v in freq.items()]
        heapq.heapify(prioirty)

        while len(prioirty) != 1:
            left = heappop(prioirty)
            right = heappop(prioirty)

            total = left.freq + right.freq
            heappush(prioirty, Node(None, total, left, right))

            # `root` stores pointer to the root of Huffman Tree
        root = prioirty[0]

        # traverse the Huffman tree and store the Huffman codes in a dictionary
        huffmanCode = {}
        encode(root, "", huffmanCode)

        for item in huffmanCode:
            a = huffmanCode[item]
            b = fixed_length(a)
            huffmanCode[item] = b

        print('--------------')
        print('Huffman Code: ')
        for i in huffmanCode:
            print(i, '->', huffmanCode[i], ' | ', end=' ')

        # print the encoded string
        str = ""
        for c in string:
            str += huffmanCode.get(c)

        print()
        print("The encoded string is ->", str)


def main():
    global length_of_string
    generated_string = generate_string(10)
    length_of_string = len(generated_string)
    print('--------------------------')
    print('Frequencies : ')
    get_frequency = calculate_frequency(generated_string)
    for i in sorted(get_frequency):
        print(i, ' | ', get_frequency[i])

    huffman(generated_string)
    print('Original values -> ', end='')
    for original_values in generated_string:
        print(original_values, end=' ')
    print()
    print('Ascii values -> ', end='')
    for ascii_values in generated_string:
        print(to_ascii(ascii_values), end=' ')
    print()


if __name__ == '__main__':
    main()
