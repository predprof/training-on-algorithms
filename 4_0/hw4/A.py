def next_step(arr, num):
    j = num - 2
    while j != -1 and arr[j] >= arr[j + 1]:
        j -= 1
    if j == -1:
        return False

    k = n - 1
    while a[j] >= a[k]:
        k -= 1

    a[j], a[k] = a[k], a[j]

    left, right = j + 1, num - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    return True


n = int(input())
a = [i for i in range(1, n + 1)]

print(''.join([str(i) for i in a]))
while next_step(a, n):
    print(''.join([str(i) for i in a]))
