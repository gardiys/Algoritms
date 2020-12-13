def evclid_nod(a,b):

    while b != 0:
        a, b = b, a % b
    return a

def nok(a,b):
    nod = evclid_nod(a, b)
    return a*b/nod


def is_prostoe(n):
    d = 2
    while d < n ** 0.5:
        if n % d == 0:
            return False
        d += 1
    return True


def all_prostoe(a):
    for i in range(2,a+1):
        if is_prostoe(i): # (O(√n * n))
            print(i)

def resheto(n):
    # 0 1 2
    # 2 3 4
    numbers = list(range(2, n+1))

    for i in range(2, int(n ** 0.5)):

        t = 2 * i

        while t <= n:
            numbers[t-2] = 0
            t += i
    return numbers

import time
start = time.time()
n = resheto(1_000_0000)
print("resheto", time.time()-start)


start = time.time()
numbers = set(n)
numbers.remove(0)

sorted(numbers) # О(n * log(n))
print("#1", time.time()-start)

start = time.time()

mass = []
for i in n:
    if i != 0:
        mass.append(i)

print("#2", time.time()-start)