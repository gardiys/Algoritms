def count_keys_equal(a, n, m):
    """
    :param a: Список чисел
    :param n: Количество элементов в списке
    :param m: Диапазон значений
    :return: Массив, который содержит количество встречавшихся чисел
    """
    equal = [0] * m

    for i in range(n):
        key = a[i]
        equal[key] += 1

    return equal


def count_less_keys(equal, m):
    """
    :param equal: Массив элементов, в которых посчитано количество
    :param m: Диапазон значений
    :return: Массив, в котором каждый элемент less[j] будет содержать сумму от 0 до j
    """
    less = [0] * m
    for j in range(1, m):
        less[j] = less[j-1] + equal[j-1]
    return less


def rearrange(a, less, n):
    """
    :param a: Массив а
    :param less: Массив полученный функцией count_less_keys
    :param n: Количество элементов в массиве
    :return: Отсортированный массив
    """
    b = [0] * n

    # Идем по массиву a и при встрече элемента смотрим на массив less. По ключу хранится позиция
    # на которую нужно поставить элемент в массиве B.
    for i in range(n):
        key = a[i]
        index = less[key]
        b[index] = a[i]
        less[key] += 1
    return b


def count_sort(a):
    equal = count_keys_equal(a, len(a), max(a)+1)
    less = count_less_keys(equal, max(a)+1)
    b = rearrange(a, less, len(a))
    return b


if __name__ == "__main__":
    from test import tester

    tester(count_sort)