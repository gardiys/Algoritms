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

a = input()
b = input()
n = len(a)
t = len(b)
z = get_z(b+"$"+a)

res = []
for i in range(t+1,n+t+1):
    if z[i] == len(b):
        res.append(i-t)
print(len(res))
print(*res)