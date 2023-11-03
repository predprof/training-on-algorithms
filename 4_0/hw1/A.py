def partition(predicat, arr, pivot, start, end):
    e = start
    g = start
    l = start
    ans = start
    for i in range(start, end):
        if predicat == 'lt':
            if arr[i] < pivot:
                arr[i], arr[g] = arr[g], arr[i]
                arr[e], arr[g] = arr[g], arr[e]
                e += 1
                g += 1
            elif arr[i] == pivot:
                arr[g], arr[i] = arr[i], arr[g]
                g += 1
            ans = e
        elif predicat == 'lte':
            if arr[i] <= pivot:
                arr[i], arr[g] = arr[g], arr[i]
                g += 1
            ans = g
        elif predicat == 'gt':
            if arr[i] > pivot:
                arr[i], arr[l] = arr[l], arr[i]
                arr[e], arr[l] = arr[l], arr[e]
                e += 1
                l += 1
            elif arr[i] == pivot:
                arr[l], arr[i] = arr[i], arr[l]
                l += 1
            ans = e
        elif predicat == 'gte':
            if arr[i] <= pivot:
                arr[i], arr[l] = arr[l], arr[i]
                l += 1
            ans = l
    return ans


n = int(input())
a = list(map(int, input().split()))
x = int(input())
ind = partition('lt', a, x, 0, n)
print(ind)
print(n - ind)
