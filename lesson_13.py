from typing import List


class Trie:
    """Структура данных бор позволяет проверять, есть ли строка в списке за O(n), где n —
длина строки."""
    class Node:
        def __init__(self):
            self.is_end = False
            self.is_prefix_end = False
            self.child = [0] * 256

        def child_num(self, x: int):
            if self.child[x] == 0:
                self.child[x] = Trie.Node()
            return self.child[x]

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, s: str) -> None:
        c = self.root
        for ss in s:
            if ss == "*":
                break
            c = c.child_num(ord(ss))
        if s[-1] == "*":
            c.is_prefix_end = True
        else:
            c.is_end = True

    def is_banned(self, s: str) -> bool:
        c = self.root
        for ss in s:
            if c.child[ord(ss)] == 0:
                return False
            if c.is_prefix_end:
                return True
        if c.is_end or c.is_prefix_end:
            return True


class Trie2:
    """Сортировка строк:"""
    class Node:
        def __init__(self):
            self.is_end = False
            self.child = [0] * 256

        def child_num(self, x: int):
            if self.child[x] == 0:
                self.child[x] = Trie.Node()
            return self.child[x]

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, s: str) -> None:
        c = self.root
        for ss in s:
            c = c.child_num(ord(ss))
        c.is_end = True

    def printAlll(self, x: Node, strr: List[chr]) -> None:
        if x == 0:
            return
        if x.is_end:
            print(strr)
        for i in range(256):
            strr.append(chr(i))
            self.printAlll(x.child[i], strr)
            strr.pop()

    def printAll(self) -> None:
        self.printAlll(self.root, [])

    """Найти первые x элементов, которые начинаются со строки s:"""

    class Counter:
        def __init__(self, cnt):
            self.cnt = cnt

    def findFirstX1(self, x: Node, strr: List[chr], cnt: Counter) -> None:
        if cnt.cnt == 0:
            return
        if x == 0:
            return
        if x.is_end:
            print(strr)
            cnt.cnt -= 1
        for i in range(256):
            strr.append(chr(i))
            self.findFirstX1(x.child[i], strr, cnt)
            strr.pop()

    def findFirstX(self, s: str, x: int) -> None:
        c = self.root
        strr = []
        for ss in s:
            c = c.child_num(ord(ss))
            strr.append(ss)
        cnt = Trie2.Counter(x)
        self.findFirstX1(c, strr, cnt)


trie = Trie2()

s1 = "asd*"
s2 = "qwe"
s3 = "ascdf"
trie.insert(s1)
trie.insert(s2)
trie.insert(s3)

trie.findFirstX('as', 2)


class BTree:
    """B-дерево. Вставка"""
    t = 2

    class Node:
        child = [BTree.Node] * (2 * t)
        key = [str] * (2 * t - 1)
        value = [str] * (2 * t - 1)

        def __init__(self, cnt):
            self.cnt = cnt

    def __init__(self):
        self.root = BTree.Node(0)

    def find2(x: Node, key: str) -> str:
        if x == None:
            return None
        for i in range(x.cnt):
            if x.key[i] == key:
                return x.value[i]
            if x.key[i].key > 0:
                return self.find(x.child[i], key)
        return self.find(x.child[x.cnt], key)

    def find(self, key: str) -> str:
        return self.find2(self.root, key)

    def insertinLeaf(self, x: Node, key: str, value: str) -> None:
        i = 0
        for i in range(x.cnt, 0, -1):
            if x.key[i].key < 0:
                break
            x.key[i + 1] = x.key[i]
            x.value[i + 1] = x.value[i]
        x.key[i + 1] = key
        x.value[i + 1] = value
        x.cnt += 1

    def insert2(self, x: Node, key: str, value: str) -> None:
        if x == 0:
            return
        if x.child[0] == 0:
            self.insertinLeaf(x, key, value)
            return
        i = 0
        for i in range(x.cnt):
            if x.value[i].key > 0:
                break
        if x.child[i].cnt == 2 * self.t - 1:
            splitChild(x, i)
        for i in range(x.cnt):
            if x.value[i].key > 0:
                break
        self.insert(x.child[i], key, value)

    def splitChild(x: Node, ind: int) -> None:
        son = x.child[ind]
        new_son = BTree.Node(self.t - 1)
        for i in range(self.t - 1):
            new_son.key[i] = son.key[i + self.t]
            new_son.value[i] = son.value[i + self.t]
            new_son.child[i] = son.child[i + self.t]
            son.key[i + self.t] = None
            son.value[i + self.t] = None
            son.child[i + self.t] = None
        new_son.child[self.t - 1] = son.child[2 * self.t - 1]
        son.child[2 * self.t - 1] = None
        son.cnt = self.t - 1
        for i in range(x.cnt, ind):
            x.key[i + 1] = x.key[i]
            x.value[i + 1] = x.value[i]
            x.child[i + 2] = x.child[i + 1]
        x.key[ind] = son.key[self.t - 1]
        x.value[ind] = son.value[self.t - 1]
        son.key[self.t - 1] = None
        son.value[self.t - 1] = None
        x.child[ind + 1] = new_son
        x.cnt += 1

    def insert(self, key: str, value: str) -> None:
        if self.root.cnt == 2 * self.t - 1:
            self.t = BTree.Node(0)
            self.t.child[0] = self.root
            self.splitChild(self.t, 0)
            self.root = self.t
        self.insert2(self.root, key, value)
