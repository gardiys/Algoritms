def merge_sort(a, p=None, r=None):
    """
    :param a: Сортируемый участок
    :param p: Левая граница участка
    :param r: Правая граница участка
    :return: Отсортированный массив
    """
    if p is None or r is None:
        p, r = 0, len(a)-1  # Начальные значения, по умолчанию r-везде включительно
    if p >= r:
        return  # Если левая граница >= правой, тогда массив уже отсортирован, тк его длина <= 1
    q = (p + r) // 2  # Середина массива
    merge_sort(a, p, q)  # Сортируем левую половину
    merge_sort(a, q+1, r)  # Сортируем правую половину
    merge(a, p, q, r)  # Склеиваем половины
    return a


def merge(a, p, q, r):
    # Используем доп память для переупорядочивания
    b = a[p:q+1] + [float('inf')]  # левая половина
    c = a[q+1:r+1] + [float('inf')]  # правая половина

    i, j = 0, 0

    for k in range(p, r+1):
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1


if __name__ == "__main__":
    from test import tester

    tester(merge_sort)
