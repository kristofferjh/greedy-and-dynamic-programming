# Author: Erlend Siqveland

import random
import heapq
from heapq import heappop, heappush

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


def encode(root, str, huffman_code):
    if root is None:
        return

    # found a leaf node
    if is_leaf(root):
        huffman_code[root.ch] = str if len(str) > 0 else '1'

    encode(root.left, str + '0', huffman_code)
    encode(root.right, str + '1', huffman_code)


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


def huffman(string):
    if len(string) == 0:
        return
    else:
        freq = calculate_frequency(string)

        prioirty = [Node(k, v) for k, v in freq.items()]
        heapq.heapify(prioirty)

        while len(prioirty) != 1:
            # Remove the two nodes of the highest priority
            # (the lowest frequency) from the queue

            left = heappop(prioirty)
            right = heappop(prioirty)

            # create a new internal node with these two nodes as children and
            # with a frequency equal to the sum of the two nodes' frequencies.
            # Add the new node to the priority queue.

            total = left.freq + right.freq
            heappush(prioirty, Node(None, total, left, right))

            # `root` stores pointer to the root of Huffman Tree
        root = prioirty[0]

        # traverse the Huffman tree and store the Huffman codes in a dictionary
        huffmanCode = {}
        encode(root, "", huffmanCode)

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
    generated_string = generate_string(10)
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