
s = input()

z = [0] * len(s)
l = r = 0
n = len(s)
for i in range(1, n):
    if i <= r:
        z[i] = min(z[i - l], r - i + 1)

    while z[i] + i < n and s[z[i]] == s[z[i] + i]:
        z[i] += 1

    if i + z[i] - 1 > r:
        l = i
        r = i + z[i] - 1

# print(*z)
max_z = 0
max_i = 0
for i in range(n - 1, -1, -1):
    if z[i] == n - i and max_z < z[i]:
        max_z = z[i]
        max_i = i
# print(max_i)

print(max_i if max_i else len(s))