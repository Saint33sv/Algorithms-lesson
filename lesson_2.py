def binary_search(int_list: list, search_int: int) -> int:
    """Алгоритм бинарного поиска (роздиляй и властвуй)"""
    left = 0
    right = len(int_list) - 1
    while left <= right:
        middle = int((left + right) / 2)
        if int_list[middle] < search_int:
            left = middle + 1
        elif int_list[middle] > search_int:
            right = middle - 1
        else:
            return middle
    return -1


l_n = [1, 2, 6, 9, 12, 23, 34, 45, 56, 67, 78, 89, 90, 114]
b_s = binary_search(l_n, 2)
print(b_s)


def remove_non_unique_numbers(num_list: list) -> list:
    """Функция удаляет из заданого списка дублирующие значения"""
    lenght = len(num_list)
    i = 0
    while i < lenght:
        found = False
        for k in range(i+1, len(num_list)):
            if num_list[i] == num_list[k]:
                found = True
                break
        if not found:
            i += 1
            continue
        else:
            num_list.pop(i)
    return num_list


some_list = [1, 2, 3, 34, 23, 1, 2, 1, 3, 34, 56, 34, 67, 4, 56, 8]
s_l = remove_non_unique_numbers(some_list)
print(s_l)


def find_spot(sort_list: list, num_for_spot: int) -> int:
    """Функция находит индекс места для вставки числа в отсортерованый список"""
    left = 0
    right = len(sort_list) - 1

    while left < right:
        middle = int((left+right) / 2)
        if sort_list[middle] < num_for_spot:
            left = middle + 1
        else:
            right = middle
    return left


sorted_list = [1100, 1200, 1600, 1600, 1600, 3000, 4000]
plase_for_spot = find_spot(sorted_list, 1600)
print(plase_for_spot)
