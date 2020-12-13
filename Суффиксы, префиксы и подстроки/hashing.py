def hash_s(s):
    k = 31
    mod = 10 ** 9 + 7
    h = 0
    m = 1

    for letter in s:
        x = ord(letter) - ord("a") + 1
        h = (h + m * x) % mod
        m = (m * k) % mod

    return h
