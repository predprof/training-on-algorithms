a = int(input())
b = int(input())
n = int(input())

b_min = b // n + int(b % n != 0)
if a > b_min:
    print('Yes')
else:
    print('No')
