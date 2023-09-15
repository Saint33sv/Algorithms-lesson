import heapq
from heapq import heappop, heappush


def rle(string: str):
    """Сжатие текстовой информации. RLE"""
    result_str = ''
    num_repit = 0
    for i in range(len(string)):
        symbol = string[i]
        if symbol not in result_str:
            result_str += symbol
            for j in range(len(string)):
                if string[j] == symbol:
                    num_repit += 1
            result_str += str(num_repit)
        num_repit = 0
    first_len = len(string)
    second_len = len(result_str)
    compression_percentage = ((first_len / second_len) * 100) - 100
    print(f"Сжатие {int(compression_percentage)}%")
    print(result_str)


a = '''Сжатие — операция, в результате которой исходное сообщение уменьшается в
объёме, но при этом качество информации сохраняется или повышается. В цифровых
системах используется два типа сжатия информации: сжатие без потерь и сжатие с
потерями.'''


def isLeaf(root):
    return root.left is None and root.right is None


class Node:
    def __init__(self, value, freq, left=None, right=None):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def encode(root, s, huffman_code):
    if root is None:
        return

    if isLeaf(root):
        huffman_code[root.value] = s if len(s) > 0 else '1'

    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)


def decode(root, index, s):
    if root is None:
        return index

    if isLeaf(root):
        print(root.value, end='')
        return index

    index += 1
    root = root.left if s[index] == '0' else root.right
    return decode(root, index, s)


def buildHuffmanTree(text):
    if len(text) == 0:
        return

    freq = {i: text.count(i) for i in set(text)}

    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)

    while len(pq) != 1:

        left = heappop(pq)
        right = heappop(pq)

        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))

    root = pq[0]

    huffmanCode = {}
    encode(root, '', huffmanCode)

    print("Коды Хаффмана для символов:", huffmanCode)
    print("Оригинальная строка:", text)

    s = ''
    for c in text:
        s += huffmanCode.get(c)

    print("Закодированая строка:", s)
    print("Декодированая строка:", end=' ')

    if isLeaf(root):
        while root.freq > 0:
            print(root.value, end='')
            root.freq -= 1
    else:
        index = -1
        while index < len(s) - 1:
            index = decode(root, index, s)


text = '00110011'
buildHuffmanTree(text)
