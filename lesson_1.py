l = [12, 35, 2, 23, 87, 56, 6, 10, 7]

# max_int = max(l)
# m = 0
# for i in l:
#    m = max(m, i)

# print(m)
# print(max_int)


def my_max(*args):
    """Функция возвращает большее число если передать в нее два числа
    или список чисел"""
    if len(args) == 1:
        max_value = 0
        for i in args[0]:
            max_value = my_max(max_value, i)
        return max_value
    if args[0] < args[1]:
        return args[1]
    else:
        return args[0]


def find_max_values(cur_list: list, int_value: int) -> int:
    """Функция возвращает максимальное число масива которое меньше заданого"""
    max_value = 0
    for i in cur_list:
        if i < int_value:
            max_value = my_max(max_value, i)
    return max_value


def list_max_values(cur_list: list, how_many_num: int) -> list:
    """Функция возвращает список заданого количества максимальных чисел,
    заданого списка"""
    curent_top = my_max(cur_list)
    list_max_nums = []
    for iteration in range(how_many_num):
        list_max_nums.append(curent_top)
        curent_top = find_max_values(cur_list, curent_top)
    return list_max_nums


list_maxes = list_max_values(l, 9)
print(list_maxes)


def unique_values(list_values: list) -> list:
    "Функия возвращает список уникальных значений из заданого списка"
    return_list = []
    for i in list_values:
        if i not in return_list:
            return_list.append(i)
    return return_list


l_v = [2, 18, "hello", 2, 14, (1, 2), "hello", 148]

r_l = unique_values(l_v)
print(r_l)


def unique_numbers_in_sorted_list(list_numbers: list) -> list:
    """Функция возвращает список уникальных чисел из заданого отсортированого списка"""
    previous_num = list_numbers[0]
    ret_list = []
    ret_list.append(previous_num)
    for i in list_numbers:
        if i != previous_num:
            ret_list.append(i)
            previous_num = i
    return ret_list


l_n = [1001, 1001, 1002, 1003, 1003, 1003, 1004, 1005, 1005, 1006]

r_l2 = unique_numbers_in_sorted_list(l_n)
print(r_l2)
