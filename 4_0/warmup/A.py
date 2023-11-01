n, m = map(int, input().split())
arr = list(map(int, input().split()))

queries = [list(map(int, input().split())) for _ in range(m)]

for q in queries:
    l, r = q[0], q[1] + 1
    min_q = min(arr[l:r])
    i = l
    while i < r and i != -1:
        if arr[i] != min_q:
            print(arr[i])
            i = -2
        i += 1
    if i != -1:
        print('NOT FOUND')
