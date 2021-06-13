def quick_sort(a, p=None, r=None):
    """
    :param a: Список чисел
    :param p: Левая граница списка
    :param r: Правая граница списка
    :return: Отсортированный список
    """
    if p is None or r is None:
        p, r = 0, len(a)-1

    if p >= r:
        return

    q = partition(a,p,r)
    quick_sort(a,p,q-1)
    quick_sort(a,q+1,r)

    return a


def partition(a,p,r):
    q = p
    # Суть цикла заключается в поиске элементов, которые меньше опорного.
    # За опорный элемент берется a[r].
    # После такого разделения мы получим элемент, который будет полностью отсортирован.
    for u in range(p, r):
        if a[u] <= a[r]:
            a[q], a[u] = a[u], a[q]
            q += 1
    a[q], a[r] = a[r], a[q]

    return q


if __name__ == "__main__":
    from test import tester

    tester(quick_sort)