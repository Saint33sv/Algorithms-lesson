from typing import List


def bubble_sort(a: List[int]) -> None:
    """Сортировка пузырьком"""
    f = True
    for j in range(len(a)):
        f = False
        for i in range(len(a)-1-j):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                f = True
        if not f:
            break


def selection_sort(a: List[int]) -> None:
    """Сортировка выбором"""
    for i in range(len(a)):
        pt = i
        for j in range(i+1, len(a)):
            if a[j] < a[pt]:
                pt = j
        a[i], a[pt] = a[pt], a[i]


def insert_into_sorted(a: List[int], x: int) -> None:
    """Вставка числа в отсортерованый список """
    pt = len(a)
    for i in range(len(a)):
        if a[i] > x:
            pt = i
            break
    a.append(0)
    for i in range(len(a)-1, pt, -1):
        a[i] = a[i-1]
    a[pt] = x


def sort_insert(a: List[int]) -> None:
    """Сортировка вставками с использованием дополнительного массива и функции
insert_into_sorted"""
    t = []
    for i in range(len(a)):
        insert_into_sorted(t, a[i])
    return t
    for j in range(len(a)):
        a[j] = t[j]


def insertion_sort(a: List[int]) -> None:
    """Алгоритм сортировки вставками без использования дополнительного массива"""
    for i in range(len(a)):
        c = a[i]
        pt = i
        while pt > 0 and a[pt-1] > c:
            a[pt] = a[pt-1]
            pt -= 1
        a[pt] = c


def sorting_numbers_by_counting(a: List[int]) -> None:
    """Алгоритм сортировки чисел подсчетом"""
    cnt = [0] * 100
    for i in range(len(a)):
        cnt[a[i]] += 1
    pt = 0
    for i in range(len(cnt)):
        for j in range(cnt[i]):
            a[pt] = i
            pt += 1


def sorting_objects_counting(a: List[int]) -> None:
    """Сортировка обьектов подсчетом параметров"""
    c = [0] * 100
    for i in range(100):
        c[i] = [0]
    for i in range(len(a)):
        c[a[i]].append(a[i])
    pt = 0
    for i in range(100):
        for j in range(1, len(c[i])):
            a[pt] = c[i].pop()
            pt += 1


def sorting_objects_counting_2(a: List[int]) -> None:
    c = [0] * 50
    for i in range(len(a)):
        c[a[i]] += 1
    print(c)
    for i in range(1, 50):
        c[i] = c[i] + c[i-1]
    print(c)
    for i in range(50-1, 0, -1):
        c[i] = c[i-1]
    print(c)
    c[0] = 0
    b = [0] * len(a)
    for i in range(len(a)):
        b[c[a[i]]] = a[i]
        c[a[i]] += 1
    for i in range(len(a)):
        a[i] = b[i]


l = [5, 2, 3, 1, 4, 7, 8, 9, 34, 6, 3, 45]
sorting_objects_counting_2(l)
print(l)
