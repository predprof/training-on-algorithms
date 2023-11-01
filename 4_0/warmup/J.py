t = int(input())
tests = []

for i in range(t):
    tests.append(tuple(map(int, input().split())))

for i in range(t):
    n, a, b = tests[i]

    k = n // b - 1
    end = n // a + 1
    flag = False
    while not flag and k <= end:
        if a * k <= n <= b * k:
            flag = True
        k += 1

    if flag:
        print('YES')
    else:
        print('NO')
