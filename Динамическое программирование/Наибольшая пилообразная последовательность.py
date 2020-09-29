n = int(input())
a = [int(i) for i in input().split()]
fp = [1]
fs = [1]
for i in range(1,n):
    max_fp = 1
    max_fs = 1
    for j in range(i):
        if a[i] > a[j] and (fs[j]+1) > max_fp:
            max_fp = fs[j] + 1
        if a[i] < a[j] and (fp[j]+1) > max_fs:
            max_fs = fp[j] + 1
    fp.append(max_fp)
    fs.append(max_fs)
print(fp)
print(fs)
print(n - max(fp[-1], fs[-1]))