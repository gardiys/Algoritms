def insertion_sort(a: [], n: int) -> []:
    """
    :param a: Список чисел
    :param n: Количество элементов
    :return: Отсортированный список
    """
    for i in range(1, n):
        j = i - 1
        while j >= 0 and a[j] > a[i]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = a[i]
    return a


if __name__ == "__main__":
    from test import tester

    tester(insertion_sort)