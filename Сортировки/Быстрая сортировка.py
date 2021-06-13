def hoar_sort(a:list) -> list:
    if len(a) <= 1:
        return a
    barrier = a[0]
    l = []
    m = []
    r = []
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    l = hoar_sort(l)
    r = hoar_sort(r)
    k = 0
    for x in l+m+r:
        a[k] = x
        k += 1
    return a

def quick_sort(a: list) -> list:
    #TODO Закончить сортировку - не рабочий вариант
    if len(a) <= 1:
        return a

    base = len(a) - 1
    r = len(a) - 2
    l = 0

    while l < r:
        while l < len(a) and a[l] < a[base]:
            l += 1

        while a[r] >= a[base] and l < r:
            r -= 1

        if l < r:
            a[l], a[r] = a[r], a[l]

    a[l], a[base] = a[base], a[l]
    return quick_sort(a[:l]) + quick_sort(a[l+1:])

print(quick_sort([3,5,8,1,2,9,4,7,6]))