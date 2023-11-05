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


def merge_sort(k, x):
    if k == 1 or k == 0:
        return x

    m = k // 2
    left = merge_sort(m, x[0:m])
    right = merge_sort(k - m, x[m::])
    result = merge(m, left, k - m, right)
    return result


n = int(input())
a = list(map(int, input().split()))
ans = merge_sort(n, a)
print(*ans)

# with open('18 (2)', 'r') as f:
#     n = int(f.readline())
#     a = list(map(int, f.read().split()))
#     ans = merge_sort(n, a)
#     print(*ans)

