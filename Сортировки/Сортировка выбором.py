def choice_sort(a: list) -> []:
    """
    :param a: Сортируемый список
    :return: Отсортированный список

    Код работает быстрее за счет того, что используются стандартные С-функции
    """
    for i in range(len(a)):
        smallest_i = a.index(min(a[i:]), i)
        a[smallest_i], a[i] = a[i], a[smallest_i]
    return a


if __name__ == "__main__":
    from test import tester
    tester(choice_sort)
