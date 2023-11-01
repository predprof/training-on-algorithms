k = int(input())
n = int(input())
staff = [0] * n

all_time = 0

for i in range(n):
    staff[i] = int(input())

for i in range(n):
    c = staff[i] // k
    all_time += 2 * c * (i + 1)
    staff[i] %= k

i = n - 1
capacity = k
while i != -1:
    # print(staff)
    if staff[i] == 0:
        i -= 1
    else:
        all_time += (i + 1)
        if staff[i] > capacity:
            staff[i] -= capacity
            all_time += 2 * (i + 1)
            capacity = k
        else:
            capacity -= staff[i]
            staff[i] = 0
            if capacity == 0:
                all_time += (i + 1)
                capacity = k
            else:
                all_time += 1
                i -= 1

print(all_time)
