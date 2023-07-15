from typing import List


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


lis = [i for i in range(1, 50)]
lower_bound(lis, -60, -1, len(lis))
