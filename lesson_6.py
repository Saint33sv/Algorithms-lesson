from queue import LifoQueue


class Queue:
    """Структура данных очередь(на зациклином масиве) где элементы добавляются в конец а 
    удаляются из начала очереди"""

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.data = [None] * max_size

    def empty(self) -> bool:
        if self.head == self.tail:
            return True
        else:
            return False

    def push_back(self, x: int) -> None:
        if self.tail + 1 == self.head or (self.tail + 1 == len(self.data) and self.head == 0):
            d = [None] * self.max_size * 2
            pt = 0
            if self.head <= self.tail:
                for i in range(self.head, self.tail):
                    d[pt] = self.data[i]
                    pt += 1
            else:
                for i in range(self.head, len(self.data)):
                    d[pt] = self.data[i]
                    pt += 1
                for i in range(0, self.tail):
                    d[pt] = self.data[i]
                    pt += 1
            self.data = d
            self.head = 0
            self.tail = pt
        self.data[self.tail] = x
        self.tail += 1
        if self.tail >= len(self.data):
            self.tail = 0

    def pop_front(self) -> int:
        if self.empty():
            print("Poping from empty queue")
            return
        t = self.data[self.head]
        self.data[self.head] = None
        self.head += 1
        if self.head >= len(self.data):
            self.head = 0
        return t

    def peek(self) -> int:
        return self.data[self.head]


class QueueStek:
    """Очередь основана на двух стеках"""

    def __init__(self):
        self.a = LifoQueue()
        self.b = LifoQueue()

    def push_back(self, x: int) -> None:
        self.a.put(x)

    def pop_front(self) -> int:
        if self.b.empty():
            while not self.a.empty():
                self.b.put(self.a.get())
        return self.b.get()


class Deque:
    """Структура данных дэк (на зациклином масиве) где элементы добавляются в конец и начало 
    удаляются из конца и  начала дэка"""

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.data = [None] * max_size

    def empty(self) -> bool:
        if self.head == self.tail:
            return True
        else:
            return False

    def double_size(self) -> None:
        d = [None] * self.max_size * 2
        pt = 0
        if self.head <= self.tail:
            for i in range(self.head, self.tail):
                d[pt] = self.data[i]
                pt += 1
        else:
            for i in range(self.head, len(self.data)):
                d[pt] = self.data[i]
                pt += 1
            for i in range(0, self.tail):
                d[pt] = self.data[i]
                pt += 1
        self.data = d
        self.head = 0
        self.tail = pt

    def push_back(self, x: int) -> None:
        if self.tail + 1 == self.head or (self.tail + 1 == len(self.data) - 1 and self.head == 0):
            self.double_size()
        self.data[self.tail] = x
        self.tail += 1
        if self.tail >= len(self.data) - 1:
            self.tail = 0

    def push_front(self, x: int) -> None:
        prev = self.head - 1
        if prev < 0:
            prev = len(self.data) - 1
        if prev == self.tail:
            self.double_size()
            prev = len(self.data) - 1
        self.data[prev] = x
        self.head = prev

    def pop_front(self) -> int:
        if self.empty():
            print("Poping from empty deque")
            return
        t = self.data[self.head]
        self.data[self.head] = None
        self.head += 1
        if self.head >= len(self.data) - 1:
            self.head = 0
        return t

    def pop_back(self) -> int:
        if self.empty():
            print("Poping from empty deque")
            return
        prev = self.tail - 1
        if prev < 0:
            prev = len(self.data) - 1
        else:
            t = self.data[prev]
            self.data[prev] = None
            self.tail = prev
            return t


class DequeStek:
    """Дэк реализован с помощью двук стеков"""

    def __init__(self):
        self.a = LifoQueue()
        self.b = LifoQueue()

    def push_back(self, x: int) -> None:
        self.a.put(x)

    def push_front(self, x: int) -> None:
        self.b.put(x)

    def rebalance(self) -> None:
        t = LifoQueue()
        s1 = self.a
        s2 = self.b
        if self.a.empty():
            s1 = self.b
            s2 = self.a
        d = s1.qsize() // 2
        for i in range(d):
            t.put(s1.get())
        while not s1.empty():
            s2.put(s1.get())
        while not t.empty():
            s1.put(t.get())

    def pop_back(self) -> int:
        if self.a.empty():
            self.rebalance()
        return self.a.get()

    def pop_front(self) -> None:
        if self.b.empty():
            self.rebalance()
        return self.b.get()


q = DequeStek()
for i in range(10):
    q.push_front(i)
print(q.pop_back())
print(q.pop_front())
