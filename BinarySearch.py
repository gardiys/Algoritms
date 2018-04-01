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


def main():
    result = ""
    a = tuple(map(int, input().split()[1:]))
    b = tuple(map(int, input().split()[1:]))
    for i in b:
        print(binary_search(i, a), end=' ')


if __name__ == "__main__":
    main()