from typing import List


class Heap:
    """Структура данных «Куча» (Heap)"""

    def __init__(self):
        self.a = []

    def size(self) -> int:
        return len(self.a)

    def get_min(self) -> int:
        return self.a[0]

    def sift_up(self, i: int) -> None:
        if i == 0:
            return
        p = (i - 1) // 2  # предок i
        if self.a[p] > self.a[i]:
            self.a[p], self.a[i] = self.a[i], self.a[p]
            self.sift_up(p)

    def add(self, x: int) -> None:
        i = len(self.a)
        self.a.append(x)
        self.sift_up(i)

    def sift_down(self, i) -> None:
        if i * 2 + 1 >= len(self.a):
            return
        l = i * 2 + 1
        r = i * 2 + 2
        min_son = l
        if r < len(self.a) and self.a[r] < self.a[l]:
            min_son = r
        if self.a[min_son] >= self.a[i]:
            return
        self.a[i], self.a[min_son] = self.a[min_son], self.a[i]
        self.sift_down(min_son)

    def pop(self) -> int:
        ret = self.a[0]
        self.a[0] = self.a[len(self.a)-1]
        self.a.pop()
        self.sift_down(0)
        return ret


def sift_up(i: int, a: List[int], size: int) -> None:
    if i == 0:
        return
    p = (i - 1) // 2
    if a[p] > a[i]:
        a[p], a[i] = a[i], a[p]
        sift_up(p, a, size)


def sift_down(i: int, a: List[int], size: int) -> None:
    if i * 2 + 1 >= size:
        return
    l = i * 2 + 1
    r = i * 2 + 2
    min_son = l
    if r < size and a[r] < a[l]:
        min_son = r
    if a[min_son] >= a[i]:
        return
    a[i], a[min_son] = a[min_son], a[i]
    sift_down(min_son, a, size)


def sort(a: List[int]) -> None:
    for i in range(len(a)):
        sift_up(i, a, i+1)
    size = len(a)
    for i in range(len(a)):
        size = len(a) - i
        a[0], a[size - 1] = a[size - 1], a[0]
        sift_down(0, a, size - 1)
    return a


def find_two_min(a: List[int]) -> None:
    m1 = a[0]
    m2 = a[1]
    if m1 > m2:
        m2, m1 = m1, m2
    for i in range(2, len(a)):
        if a[i] > m2:
            continue
        if a[i] < m1:
            m2 = m1
            m1 = a[i]
        elif a[i] < m2:
            m2 = a[i]
    print(m1)
    print(m2)


class Task:
    def __init__(self, ident, priority):
        self.ident = ident
        self.priority = priority


class HeapQueue:
    """Очередь с приоритетами, в которой каждый элемент имеет идентификатор и
приоритет. Чем меньше приоритет, тем раньше выполняется задача"""

    def __init__(self):
        self.a = []
        self.pos = [0] * 1000

    def size(self) -> int:
        return len(self.a)

    def get_min(self) -> int:
        return self.a[0].ident

    def sift_up(self, i: int) -> None:
        if i == 0:
            return
        p = (i - 1) // 2  # предок i
        if self.a[p].priority > self.a[i].priority:
            self.a[p], self.a[i] = self.a[i], self.a[p]
            self.pos[self.a[i].ident] = i
            self.pos[self.a[p].ident] = p
            self.sift_up(p)

    def push(self, t: Task) -> None:
        i = len(self.a)
        self.pos[t.ident] = i
        self.a.append(t)
        self.sift_up(i - 1)

    def sift_down(self, i) -> None:
        if i * 2 + 1 >= len(self.a):
            return
        l = i * 2 + 1
        r = i * 2 + 2
        min_son = l
        if r < len(self.a) and self.a[r].priority < self.a[l].priority:
            min_son = r
        if self.a[min_son].priority >= self.a[i].priority:
            return
        self.a[i], self.a[min_son] = self.a[min_son], self.a[i]
        self.pos[self.a[i].ident] = i
        self.pos[self.a[min_son].ident] = min_son
        self.sift_down(min_son)

    def pop(self) -> int:
        ret = self.a[0]
        self.a[0] = self.a[len(self.a)-1]
        self.a.pop()
        self.pos[self.a[0]] = 0
        self.sift_down(0)
        return ret

    def set_priority(self, ident, priority: int) -> None:
        p = self.pos[ident]
        self.a[p].priority = priority
        self.sift_down(p)
        self.sift_up(p)


hq = HeapQueue()

l = [2, 1, 4, 6, 8, 5, 23, -4]
for i, p in enumerate(l):
    t = Task(i, p)
    hq.push(t)

print(hq.get_min())
