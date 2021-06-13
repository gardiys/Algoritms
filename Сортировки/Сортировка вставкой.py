def insertion_sort(a: []) -> []:
    """
    :param a: Список чисел
    :param n: Количество элементов
    :return: Отсортированный список
    """
    for i in range(1, len(a)):
        j = i - 1
        key = a[i]
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a


if __name__ == "__main__":
    from test import tester

    tester(insertion_sort)