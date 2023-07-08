class DLList:
    """Двухсвязный список"""
    class Node:
        """Элемент списка"""

        def __init__(self, x: int):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self):
        self.start = DLList.Node(None)
        self.end = DLList.Node(None)

    def printt(self) -> None:
        """Вывести список на экран"""
        t = self.start
        while t != None:
            print(t.x)
            t = t.next

    def push_front(self, x: int) -> None:
        """Вставить элемент в начало списка"""
        t = DLList.Node(x)
        if self.start.x == None:
            self.start = t
            self.end = t
            return
        t.next = self.start
        self.start.prev = t
        self.start = t

    def insert(self, v: Node, x: int) -> None:
        """Вставить элемент в середину списка"""
        t = DLList.Node(x)
        next_el = v.next
        if next_el == None:
            t.next = None
            v.next = t
            t.prev = v
            self.end = t
            return
        next_el.prev = t
        t.next = next_el
        v.next = t
        t.prev = v

    def push_back(self, x: int) -> None:
        """Вставка элемента в конец спика"""
        if self.end.x == None:
            t = DLList.Node(x)
            self.start = t
            self.end = t
            return
        self.insert(self.end, x)

    def delete(self, v: Node) -> None:
        prev = v.prev
        nextt = v.next
        if prev != None:
            prev.next = nextt
        if nextt != None:
            nextt.prev = prev
        v.next = None
        v.prev = None
        if v == self.start:
            self.start = nextt
        if v == self.end:
            self.end == prev

    def pop_front(self) -> None:
        self.delete(self.start)

    def pop_back(self) -> None:
        self.delete(self.end)

    def merge(self, l) -> None:
        """Соединить два списка"""
        if l.start == None:
            return
        if self.end == None:
            self.start = l.start
            self.end = l.end
            return
        self.end.next = l.start
        l.start.prev = self.end
        self.end = l.end

    def revert_rec(self, v: Node) -> Node:
        """Рекурсивная функция переворота списка"""
        if v == None:
            return None
        t = self.revert_rec(v.next)
        if t != None:
            t.next = v
        v.prev = t
        return v

    def revert_slow(self) -> None:
        """Переворот списка с помощью рекурсивной функции"""
        tmp = self.revert_rec(self.start)
        tmp.next = None
        t = self.start
        self.start = self.end
        self.end = t

    def revert(self) -> None:
        """Разворот списка без приминения рекурсии"""
        a = self.start
        b = self.start.next
        a.next = None
        if b != None:
            c = b.next
        while b != None:
            a.prev = b
            b.next = a
            a = b
            b = c
            if c != None:
                c = c.next
        a.prev = None
        t = self.start
        self.start = self.end
        self.end = t

    def find_cycle(self) -> None:
        """Поиск зацикленности списка"""
        a = self.start
        b = self.start
        while True:
            if b == None:
                break
            b = b.next
            if a == b:
                break
            if b == None:
                break
            b = b.next
            if a == b:
                break
            a = a.next
        if b == None:
            print("No cycle")
            return
        b = b.next
        while a != b:
            print(b.x)
            b = b.next
        print(b.x)


l_list = DLList()
l_2 = DLList()
for i in range(30, 45):
    l_2.push_front(i)
l_2.start.prev = l_2.end
l_2.end.next = l_2.start


l_list.push_back(6)
l_list.push_back(9)
l_list.push_front(12)
l_list.push_front(23)
l_list.merge(l_2)
l_list.find_cycle()
# l_list.printt()
