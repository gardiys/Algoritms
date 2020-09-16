def binary_search(k, a):

    l, r = 0, len(a) - 1
    while l <= r:
        m = l + (r - l) // 2
        if k == a[m]:
            return m + 1
        elif k > a[m]:
            l = m + 1
        else:
            r = m - 1
    return -1

def binary_search_with_counting(k, a, last:bool):
    n = len(k)
    l, r = 0, len(a) - 1
    while l <= r:
        m = l + (r - l) // 2
        if k > a[m] or last and k == a[m]:
            l = m + 1
        elif k < a[m] or (not last) and k == a[m]:
            r = m - 1
    return r if last else l


def main():
    result = ""
    a = tuple(map(int, input().split()[1:]))
    b = tuple(map(int, input().split()[1:]))
    for i in b:
        print(binary_search(i, a), end=' ')

def main2():
    a = input()
    pattern = input()
    right = binary_search(pattern,a,True)
    left = binary_search(pattern,a,False)
    print(right - left + 1)

if __name__ == "__main__":
    main()