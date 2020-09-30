s = list(input())

s += reversed(s)
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
print(z)
print(max(z[n // 2:]))