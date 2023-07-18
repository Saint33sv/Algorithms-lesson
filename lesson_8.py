from typing import List
import string


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


def marge(a, b: List[int]) -> List[int]:
    """Рекурсивная функция для слияния двух отсортированых масивов"""
    p1 = 0
    p2 = 0
    res = []
    while p1 < len(a) or p2 < len(b):
        if p1 == len(a):
            res.append(b[p2])
            p2 += 1
            continue
        if p2 == len(b):
            res.append(a[p1])
            p1 += 1
            continue
        if a[p1] < b[p2]:
            res.append(a[p1])
            p1 += 1
        else:
            res.append(b[p2])
            p2 += 1
    return res


def sorted_m(a: List[int]) -> List[int]:
    if len(a) == 1:
        return a
    m = len(a) // 2
    l = sorted_m(a[:m])
    r = sorted_m(a[m:])
    print(l, "\n", r)
    marge(l, r)


lis = [1, 2, 7, 4, 56, 2, 5, 8, 76, 34, 6, 5, 2, 5, 9, 4]

sorted_m(lis)
