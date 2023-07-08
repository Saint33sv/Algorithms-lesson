class DynamicArray:
    """Пример динамического масива """

    def __init__(self):
        self.data = [None] * 1
        self.lenght = 0

    def show(self) -> list:
        return self.data

    def size(self) -> int:
        return self.lenght

    def sett(self, ind: int, value: int) -> None:
        self.data[ind] = value

    def get(self, ind: int) -> int:
        return self.data[ind]

    def add(self, x: int) -> None:
        lenn = len(self.data)
        if self.lenght == lenn:
            new_data = [None] * (lenn * 2)
            for i in range(self.lenght):
                new_data[i] = self.data[i]
            self.data = new_data
        self.data[self.lenght] = x
        self.lenght += 1

    def remove(self) -> None:
        self.lenght -= 1
        lenn = len(self.data)
        if self.lenght*4 <= lenn:
            new_data = [None] * (lenn/2)
            for i in range(self.lenght):
                new_data[i] = self.data[i]
            self.data = new_data

    def insert(self, x: int, ind: int) -> None:
        self.add(0)
        for i in range(self.lenght-1, ind, -1):
            self.data[i] = self.data[i-1]
        self.data[ind] = x


class Node:
    """Пример односвязного списка"""

    def __init__(self, x: int):
        self.x = x
        self.next_node = None


# start = Node(None)
#
# for i in range(11):
#    n = Node(i)
#    n.next_node = start
#    start = n
#
# summ = 0
# t = Node(None)
# t = start
#
# while t.next_node != None:
#    summ += t.x
#    t = t.next_node
# print(summ)


def check(s: str) -> bool:
    """Задача проверки на правильность скобочной последовательности с тремя видами
скобок: (){}[]:"""
    str_list = []
    for i in s:
        if i in ['(', '{', '[']:
            str_list.append(i)
        else:
            if not str_list:
                return False
            if i == ')' and str_list[-1] == '(':
                str_list.pop()
            if i == '}' and str_list[-1] == '{':
                str_list.pop()
            if i == ']' and str_list[-1] == '[':
                str_list.pop()
    if str_list:
        return False
    return True


print(check("({()])"))
