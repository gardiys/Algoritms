def get_random_mass(n):
    import random
    a = [0] * n
    for i in range(n):
        a[i] = random.randint(-1000, 1000)
    return a


def test_correct(func):
    assert func([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert func([3, 2, 4, 5, 1]) == [1, 2, 3, 4, 5]
    assert func([1, 1, 3, 3, 2]) == [1, 1, 2, 3, 3]
    assert func([5, 5, 7, 7, 4]) == [4, 5, 5, 7, 7]
    mass = get_random_mass(1000)
    assert func(mass) == sorted(mass)
    print("Сортировка работает корректно")



def test_time(func):
    import time
    a1 = get_random_mass(100)
    a2 = get_random_mass(1000)
    a3 = get_random_mass(10_000)
    a4 = get_random_mass(100_000)

    start = time.time()
    func(a1)
    print('10**2:', time.time() - start)

    start = time.time()
    func(a2)
    print('10**3:', time.time() - start)

    start = time.time()
    func(a3)
    print('10**4:', time.time() - start)

    start = time.time()
    func(a4)
    print('10**5:', time.time() - start)


def tester(func):
    test_correct(func)
    test_time(func)
