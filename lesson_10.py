from typing import List


class Node:
    def __init__(self, x, parent):
        self.x = x
        self.parent = parent
        self.l = None
        self.r = None


class Tree:
    def __init__(self):
        self.root = None

    def add_recursively(v: Node, x: int) -> None:
        if v == None:
            return
        if x < v.x:
            if v.l == None:
                v.l = Node(x, v)
                return
            add_recursively(v.l, x)
        else:
            if v.r == None:
                v.r = Node(x, v)
                return
            add_recursively(x.r, x)

    def add(self, x: int) -> None:
        """Поиск места для добавления элемента в двоичное дерево поиска (не
сбалансированное)"""
        if self.root == None:
            self.root == Node(x, None)
            return
        self.add_recursively(self.root, x)

    def from_array_recursively(self, a: List[int], l, r: int) -> Node:
        if l + 1 > r:
            return None
        if l + 1 == r:
            return Node(a[l], None)
        m = (l + r) >> 1
        t = Node(a[m], None)
        t.l = self.from_array_recursively(a, l, m)
        t.r = self.from_array_recursively(a, m+1, r)
        if t.l != None:
            t.l.parent = t
        if t.r != None:
            t.r.parent = t
        return t

    def from_array(self, a: List[int]):
        """Построение сбалансированного двоичного дерева поиска из отсортированного
        массива"""
        res = Tree()
        res.root = self.from_array_recursively(a, 0, len(a))
        return res

    def find_recursively(self, v: Node, x: int) -> Node:
        if v == None:
            return None
        if v.x == x:
            return v
        if v.x > x:
            return self.find_recursively(v.l, x)
        else:
            return self.find_recursively(v.r, x)

    def find(self, x: int) -> Node:
        return self.find_recursively(self.root, x)

    def delete_recursively(self, t: Node) -> None:
        if t == None:
            return
        if t.l == None or t.r == None:
            child = None
            if t.l != None:
                child = t.l
            else:
                child = t.r
            if t == self.root:
                self.root = child
                if child != None:
                    child.parent = None
            if t.parent.l == t:
                t.parent.l = child
                if child != None:
                    child.parent = t.parent
            else:
                t.parent.r = child
                if child != None:
                    child.parent = t.parent
        else:
            nxt = t.r
            while nxt.l != None:
                nxt = nxt.l
            t.x = nxt.x
            self.delete_recursively(nxt)

    def delete(self, x: int) -> None:
        if self.root == None:
            return
        t = self.find(x)
        if t == None:
            return
        self.delete_recursively(t)

    def next(self, v: Node) -> Node:
        """Найти следующий узел"""
        if v == None:
            return None
        if v.r != None:
            nxt = v.r
            while nxt.l != None:
                nxt = nxt.l
            return nxt
        nxt = v
        while nxt.parent != None and nxt.parent.r == nxt:
            nxt = nxt.parent
        return nxt.parent

    def previous(self, v: Node) -> Node:
        """Найти предидущий узел"""
        if v == None:
            return None
        if v.l != None:
            prev = v.l
            while prev.r != None:
                prev = prev.r
            return prev
        prev = v
        while prev.parent != None and prev.parent.l == prev:
            prev = prev.parent
        return prev.parent

    def print_tree(self, v: Node) -> None:
        if v == None:
            return
        self.print_tree(v.l)
        print(v.x)
        self.print_tree(v.r)

    def printt(self) -> None:
        self.print_tree(self.root)

    def check2(self, v: Node, l, r: None) -> bool:
        if v == None:
            return True
        if l != None and v.x < l:
            return False
        if r != None and v.x > r:
            return False
        return self.check2(v.l, l, v.x) and self.check2(v.r, v.x, r)

    def check(self) -> bool:
        return self.check2(self.root, None, None)


tr = Tree()
a = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]

r = tr.from_array(a)
print(r.check())
