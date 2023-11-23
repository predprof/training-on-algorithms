k = int(input())
n = int(input())
employees = [int(input()) for _ in range(n)]

time, current = 0, n
while current > 0:
    time += 2 * current * (employees[current - 1] // k)

    left = employees[current - 1] % k
    if left != 0:
        time += 2 * current
        current -= 1
        while left < k and current > 0:
            if k - left >= employees[current - 1]:
                left += employees[current - 1]
                employees[current - 1] = 0
                current -= 1
            else:
                employees[current - 1] -= k - left
                left = k
    else:
        current -= 1

print(time)

# доработать
# k = int(input())
# n = int(input())
# staff = [0] * n
#
# all_time = 0
#
# for i in range(n):
#     staff[i] = int(input())
#
# for i in range(n):
#     c = staff[i] // k
#     all_time += 2 * c * (i + 1)
#     staff[i] %= k
# # print(all_time)
# i = n - 1
# capacity = k
# while i != -1:
#     # print(staff)
#     if staff[i] == 0:
#         i -= 1
#         all_time += 1
#     else:
#         if capacity == k:
#             all_time += (i + 1)
#         if staff[i] > capacity:
#             staff[i] -= capacity
#             all_time += (i + 1)
#             capacity = k
#         else:
#             capacity -= staff[i]
#             staff[i] = 0
#             if capacity == 0:
#                 all_time += (i + 1)
#                 capacity = k
#             else:
#                 all_time += 1
#                 i -= 1
#
# print(all_time)
