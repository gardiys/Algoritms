a = input()
b = input()

n, m = len(a), len(b)

f = []
for i in range(n+1):
    f.append([0]*(m+1))

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1] == b[j-1] and i == j:
            f[i][j] = 1
        elif a[i-1] == "?" and i == j:
            f[i][j] = 1
        elif a[i-1] == "*" and j >= i-1:
            f[i][j] = 1
        else:
            f[i][j] = 0

print(*f, sep="\n")