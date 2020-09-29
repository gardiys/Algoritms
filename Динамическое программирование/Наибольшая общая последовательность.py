a = input()
b = input()

n, m = len(a), len(b)

f = []
for i in range(n+1):
    f.append([0]*(m+1))

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1] == b[j-1]:
            f[i][j] = f[i-1][j-1] + 1
        else:
            f[i][j] = max(f[i-1][j],f[i][j-1])
#print(f)
i = n
j = m
ans_a = []
ans_b = []
while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
        ans_a.append(i)
        ans_b.append(j)
        i -= 1
        j -= 1
    elif f[i][j-1] == f[i][j]:
        j -= 1
    else:
        i -= 1
print(len(ans_a))
print(*ans_a[::-1])
print(*ans_b[::-1])
