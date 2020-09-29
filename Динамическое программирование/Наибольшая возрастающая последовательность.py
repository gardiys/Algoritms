n = int(input())
a = [int(i) for i in input().split()]
f = [0] * n
p = [-1] * n
for i in range(n):
    max_el = 0
    for j in range(i):
        if a[j] < a[i] and f[j] > f[i]:
            f[i] = f[j]
            p[i] = j
    f[i] += 1

max_el = max(f)
print(max_el)
i = f.index(max_el)
ans = []
while i != -1:
    ans.append(a[i])
    i = p[i]
print(*ans[::-1])