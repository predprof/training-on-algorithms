def merge(k, x, p, y):
    result = []
    i = 0
    j = 0
    while i < k and j < p:
        if x[i] < y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1

    if i == k:
        result.extend(y[j::])
    else:
        result.extend(x[i::])
    return result


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = merge(n, a, m, b)
print(*ans)
