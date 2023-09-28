def move_null(a_list: list) -> list:
    """Алгоритм смещения нулей в списке в конец"""
    if len(a_list) == 0:
        return a_list
    zero_index = 0
    for index, value in enumerate(a_list):
        if value != 0:
            a_list[zero_index] = value
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return a_list


def even_odd_numbers(a_list: list) -> list:
    """Алгоритм возвращает список где все нечетные числа идут после четных"""
    even = []
    odd = []
    for num in a_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    result = even + odd
    return result


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = even_odd_numbers(a)
print(res)
