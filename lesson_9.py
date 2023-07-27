from typing import List
import random


def solve(tasks: List[int], work_time: int) -> int:
    """Жадный алгоритм:
Есть N задач, чтобы решить любую из этих задач, требуется один час. За решение задачи
под номером i, вы получаете c[i] монет. Как получить максимальное количество монет, если
у вас есть всего К свободных часов?
Нужно взять К задач, которые дают максимальное количество монет. Для этого можно K раз
выбрать из оставшихся невыполненных задач ту, которая даёт больше всего монет (жадно
берём каждый раз задачу, которая даст самое большое количество монет в данный момент,
а что будет дальше — не думаем)"""
    tasks.sort(reverse=True)
    sum = 0
    for i in range(work_time):
        if i >= work_time:
            break
        sum += tasks[i]
    return sum


class Segment:
    def __init__(self, l, r: int):
        self.l = l
        self.r = r


def solve_segments(segments: List[Segment]) -> int:
    """Есть N полосок на одной прямой, у каждой полоски есть координата начала и конца —
l[i] и r[i]. Нужно выбрать максимальное количество полосок так, чтобы выбранные
полоски не пересекались.
Решение: сортировать отрезки по координате конца. После этого идти по ним
отсортированным, и, если выбираем текущий отрезок и он не пересечётся с последним,
который мы взяли, то берём его:"""
    if not segments:
        return 0
    segments.sort(key=lambda x: x.r)
    last_r = segments[0].l
    ans = 0
    for i in range(len(segments)):
        if segments[i].l >= last_r:
            ans += 1
            last_r = segments[i].r
    return ans


def solve_slow(segments: List[Segment]) -> int:
    """медленое решение задачи про полоски"""
    ans = 0
    for mask in range(1 << len(segments)):
        intersect = False
        for i in range(len(segments)):
            for j in range(i+1, len(segments)):
                if mask & (1 << i) == 0 or mask & (1 << j) == 0:
                    continue
                l = max(segments[i].l, segments[j].l)
                r = min(segments[i].r, segments[j].r)
                if l < r:
                    intersect = True
                    break
        if not intersect:
            cnt = 0
            for i in range(len(segments)):
                if mask & (1 << i) > 0:
                    cnt += 1
            if cnt > ans:
                ans = cnt
    return ans


def gen() -> List[Segment]:
    """список обьектов для теста"""
    test = []
    n = random.randint(1, 10)
    for i in range(n):
        r = random.randint(1, 100)
        l = random.randint(r, 101)
        test.append(Segment(l, r))
    return test


def stress_test() -> None:
    """Стресс-тестирование — один из видов тестирования программ, заключающийся в
сравнении результатов простого, верного, но не оптимального решения задачи с
результатом «быстрого» решения, в котором есть сомнения. Сравнение
осуществляется с помощью генерации случайных тестов. Если ответ на каком-то тесте
отличается, то это является основанием для поиска ошибок в коде. 
Стресстестирование можно провести не только при сомнении в правильности алгоритма, но и
в случае сложной реализации алгоритма для поиска ошибок."""
    while True:
        test = gen()
        if solve_slow(test) != solve_segments(test):
            print("Stress failed")
            print(len(test))
            for i in range(len(test)):
                print(test[i].l + " " + test[i].r)
                print(" ")


class Box:
    def __init__(self, w, m):
        """w — вес коробки, m —
максимальный суммарный вес коробок, который можно поставить на эту коробку сверху"""
        self.w = w
        self.m = m


def solve_box(boxes: List[Box]) -> int:
    """Задача с коробками"""
    boxes.sort(key=lambda x: (x.w + x.m))
    q = []
    sum_w = 0
    cnt = 0
    for i in range(len(boxes)):
        if boxes[i].m >= sum_w:
            cnt += 1
            sum_w += boxes[i].w
            q.append(boxes[i])
            q.sort(key=lambda x: x.w, reverse=True)
        else:
            if q[-1].w > boxes[i].w:
                sum_w -= q.pop().w
                q.pop()
                q.append(boxes[i])
                q.sort(key=lambda x: x.w, reverse=True)
                sum_w += boxes[i].w
    for i in q:
        print((i.w, i.m))
    return cnt


class Node:
    def __init__(self, w, zero, one, c):
        self.w = w
        self.zero = zero
        self.one = one
        self.c = c


def dfs(x: Node, res: List[int]) -> None:
    if x.zero == None:
        print(f"Code for {x.c}:")
        for i in range(len(res)):
            print(res[i])
        return
    res.append(0)
    dfs(x.zero, res)
    res.pop()
    res.append(1)
    dfs(x.one, res)


def huffman(s: str) -> None:
    a = [0]*256
    for i in range(len(s)):
        a[ord(s[i])] += 1  # вычисление количества вхождения символа
    q = []  # список с узлами символов
    for i in range(256):
        if a[i] > 0:
            # заполняем список символами которые в строке
            q.append(Node(a[i], None, None, chr(i)))
    q.sort(key=lambda x: x.w, reverse=True)  # сортируем по убыванию вхождений
    while len(q) > 1:
        print(q[-1].c)
        t1 = q.pop()
        t2 = q.pop()  # берем два последних элемента
        # создаем узел из послелних элементов
        n = Node(t1.w + t2.w, t2, t1, '\0')
        q.append(n)  # добавляем узел в список
    dfs(q[0], [])  # запуск рекурсивной функции


st = 'Hello World'
huffman(st)
