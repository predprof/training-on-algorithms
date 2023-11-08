def ispattern(l, from1, from2):
    return (
            ((h[from1 + l - 1] + h[from2 - 1] * xarr[l]) % p) ==
            ((h[from2 + l - 1] + h[from1 - 1] * xarr[l]) % p)
    )


s = input()

n = len(s)
p = 10 ** 9 + 7
x = 257
h = [0] * (n + 1)
xarr = [0] * (n + 1)
xarr[0] = 1
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x + ord(s[i - 1])) % p
    xarr[i] = (xarr[i - 1] * x) % p

for k in range(1, n + 1):
    i = 1
    flag = True
    while flag and i < n + 2 - k:
        if not ispattern(k, 1, i):
            flag = False
        i += k

    if not ispattern(n % k, 1, k * (n // k) + 1):
        flag = False

    if flag:
        print(k)
        break




