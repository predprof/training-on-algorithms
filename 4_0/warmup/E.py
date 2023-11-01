n = int(input())
rates = list(map(int, input().split()))

sums = [0] * n
sums[0] = rates[0]
for i in range(1, n):
    sums[i] = sums[i - 1] + rates[i]

hates = [0] * n
for i in range(n):
    if i == 0:
        hates[i] = sums[n - 1] - sums[i] - (n - 1) * rates[i]
    else:
        hates[i] = (2 * i + 1 - n) * rates[i] - sums[i] + (sums[n - 1] - sums[i - 1])

print(*hates)
