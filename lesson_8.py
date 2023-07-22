from typing import List
import string
import random


def lower_bound(a: List[int], key: int, l: int, r: int) -> None:
    """Рекурсивный бинарный алгоритм"""
    if l + 1 >= r:
        print(r)
        return
    m = int((l+r) / 2)
    if a[m] > key:
        lower_bound(a, key, l, m)
    elif a[m] < key:
        lower_bound(a, key, m, r)
    else:
        print(m)
        return


NUMBERS = '0123456789'


def line_selection() -> None:
    """Подбор строки состоящией из маленьких букв"""
    itr = 0
    for s1 in string.ascii_uppercase:
        itr += 1
        for s2 in string.ascii_uppercase:
            itr += 1
            for s3 in string.ascii_uppercase:
                itr += 1
                for s4 in string.ascii_uppercase:
                    itr += 1
                    print(s1, s2, s3, s4)
    print(f"всего вариантов: {itr}")


def small_capital_leters_and_numbers() -> None:
    """Подбор строки (пароля) состоящий из больших маленьких букв и цыфр"""
    possible = []
    itr = 0
    for i in string.ascii_letters:
        possible.append(i)
    for i in NUMBERS:
        possible.append(i)
    for s1 in possible:
        itr += 1
        for s2 in possible:
            itr += 1
            for s3 in possible:
                itr += 1
                for s4 in possible:
                    itr += 1
                    print(s1, s2, s3, s4)
    print(f"всего вариантов: {itr}")


def gen(c, n: int, l: list) -> None:
    """Рекурсивный перебор всех паролей длины n, начиная с позиции символа с"""
    if c == n:
        print(l)
        return
    for l[c] in string.ascii_lowercase:
        if c > 0 and l[c] == l[c-1]:  # если в пароле не двух подряд одинаковых символов
            continue
        gen(c+1, n, l)


class Bitset:
    """Битовая маска, которая умеет хранить массив из 0 и 1, используя на каждый индекс 1
бит памяти"""

    def __init__(self, n: int):
        self.data = [0] * (n // 32 + 1)

    def get(self, ind: int) -> int:
        x = self.data[ind // 32]
        return (x >> (ind % 32)) & 1

    def set(self, ind, val: int) -> None:
        if self.get(ind) == val:
            return
        self.data[ind//32] ^= 1 << (ind % 32)


a = Bitset(1)


def gen_lamp(x, n, k: int) -> None:
    """Задача перебрать все возможные варианты зажжения k лампочек из n возможных (все
возможные массивы из 0 и 1 длины n, в которых ровно k единиц)"""
    if k < 0:
        return
    if k > (n-x):
        return
    if x == n:
        for i in range(n):
            print(a.get(i))
        print(' ')
        return
    a.set(x, 0)
    gen_lamp(x+1, n, k)
    a.set(x, 1)
    gen_lamp(x+1, n, k-1)


def hanoi(n: int, fromm, to, aux: chr) -> None:
    """Функция, показывающая решение головоломки «Ханойская башня»"""
    if n == 1:
        print('Move ring', n, 'from', fromm, 'to', to)
        return
    hanoi(n-1, fromm, aux, to)
    print('Move ring', n, 'from', fromm, 'to', to)
    hanoi(n-1, aux, to, fromm)


def marge(a: List[int], l, m, r: int, buf: List[int]) -> None:
    """Рекурсивная функция для слияния двух отсортированых масивов"""
    p1 = l
    p2 = m
    rp = 0
    while p1 < m or p2 < r:
        if p1 == m:
            buf[rp] = a[p2]
            p2 += 1
            rp += 1
            continue
        if p2 == r:
            buf[rp] = a[p1]
            p1 += 1
            rp += 1
            continue
        if a[p1] < a[p2]:
            buf[rp] = a[p1]
            p1 += 1
            rp += 1
        else:
            buf[rp] = a[p2]
            p2 += 1
            rp += 1
    for i in range(l, r):
        a[i] = buf[i - l]


def sorted_m(a: List[int], l, r: int, buf: List[int]) -> None:
    """Рекурсивная сортировка слиянием"""
    if r - l <= 1:
        return
    m = (r + l) // 2
    sorted_m(a, l, m, buf)
    sorted_m(a, m, r, buf)
    marge(a, l, m, r, buf)


def sort_m(a: List[int]) -> None:
    buf = [0] * len(a)
    sorted_m(a, 0, len(a), buf)


def partition(a: List[int], l, r: int) -> int:
    """Функция partition, которая в левую половину перемещает все элементы меньше либо
равные, а в правую больше либо равные медиане"""
    if r - l < 1:
        return l
    i = l
    j = r-1
    x = a[l + random.randint(0, (r - l))]
    while i < j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            break
    return i


def qsort(a: List[int], l, r: int) -> None:
    """Функция быстрой сортировки"""
    if (r - l) <= 1:
        return
    m = partition(a, l, r)
    qsort(a, m, r)
    qsort(a, l, m)


def ktm_element(a: List[int], k: int) -> int:
    """Для поиска k-ой порядковой статистики можно рекурсивно разбивать массив на две
части, где в левой все элементы меньше или равны элементам правой части"""
    l = 0
    r = len(a)
    while l + 1 < r:
        m = partition(a, l, r)
        if k >= m:
            l = m
        else:
            r = m
    return a[l]


def median(a: List[int]) -> int:
    """Вариант поиска медианы"""
    return ktm_element(a, len(a) // 2)


l = [7, 4, 6, 45, 2, 7, 6, 78, 65, 2, 1, 4, 56, 8, 9]

m = median(l)
print(m)
