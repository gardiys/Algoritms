def get_z(s):
    n = len(s)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if r >= i:
            z[i] = min(z[i - l], r - i + 1)

        while z[i] + i < n and s[z[i]] == s[z[i] + i]:
            z[i] += 1

        if z[i] + i - 1 > r:
            l = i
            r = z[i] + i - 1
    return z

# Количество различных подстрок в строке за O(n^2)
s = input()
n = len(s)
k = 1
p = s[0]
for i in range(1,n):
    p += s[i]
    z = max(get_z(p[::-1]))
    k += len(p)-z
print(k)

