def phase(num, arr):
    buckets = {j: [] for j in range(10)}
    for number in arr:
        buckets[int(number[-num])].append(number)
    return buckets


with open('test', 'r') as f:
    n = int(f.readline())
    a = [''] * n
    for i in range(n):
        a[i] = f.readline().strip()

print('Initial array:')
print(', '.join(a))
print('**********')

current = {}
answer = []
for m in range(1, len(a[0]) + 1):
    print(f'Phase {m}')
    if m == 1:
        current = phase(m, a)
    else:
        numbers = []
        for i in range(10):
            numbers.extend(current[i])
        current = phase(m, numbers)
    for i in range(10):
        if not current[i]:
            print(f'Bucket {i}: empty')
        else:
            print(f'Bucket {i}:', ', '.join(current[i]))
        if m == len(a[0]):
            answer += current[i]
    print('**********')

print('Sorted array:')
print(', '.join(answer))