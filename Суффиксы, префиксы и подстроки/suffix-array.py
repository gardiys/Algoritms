def count_sort(p:list, c:list):
    n = len(p)

    cnt = [0] * n
    for i in c:
        cnt[i] += 1

    pos = [0] * n
    p_new = [0] * n

    for i in range(1,n):
        pos[i] = pos[i-1] + cnt[i-1]

    for x in p:
        i = c[x]
        p_new[pos[i]] = x
        pos[i] += 1

    p = p_new

    return p, c


def get_suffix_array(s:str):
    s += "$"
    n = len(s)
    c = [0]*n
    a = sorted([(s[i],i) for i in range(n)])

    p = [a[i][1] for i in range(n)]

    for i in range(1,n):
        if a[i][0] == a[i-1][0]:
            c[p[i]] = c[p[i-1]]
        else:
            c[p[i]] = c[p[i-1]] + 1

    k = 1
    while k < n:
        a = []
        # for i in range(n):
        #     a.append(((c[i], c[(i + k) % n]),i))
        for i in range(n):
            p[i] = (p[i] - k + n) % n
        p, c = count_sort(p, c)
        c_new = [0]*n

        for i in range(1, n):
            pre = (c[p[i - 1]], c[(p[i - 1] + k) % n])
            now = (c[p[i]], c[(p[i] + k) % n])
            if pre == now:
                c_new[p[i]] = c_new[p[i - 1]]
            else:
                c_new[p[i]] = c_new[p[i - 1]] + 1

        c = c_new
        k *= 2

    # for i in p:
    #     print(s[i:])

    return p


if __name__ == "__main__":
    print(*get_suffix_array(input()))