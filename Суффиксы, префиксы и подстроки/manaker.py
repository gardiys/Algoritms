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

def binary_search(s:str,center:int,shift:int):
    # shift = 0 при поиске палиндрома нечетной длины, иначе shift = 1
    l = -1
    r = min(center, len(s)-center+shift)
    m = 0
    while r-l != 1:
        m = l + (r-l) // 2

        # reversed_hash возвращает хэш развернутой строки s
        if hash_s(s[center-m:center]) == hash_s(reversed(s[center+shift:center+shift+m])):
            l = m
        else:
            r = m
    return r

def palindromes_count(s:str):
    ans = 0
    for i in range(len(s)):
        ans += binary_search(s,i,0) + binary_search(s,i,1)
    return ans

