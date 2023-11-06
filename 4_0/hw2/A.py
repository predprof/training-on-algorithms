def equal(l, s1, s2):
    k = 0
    while k < l and s1[k] == s2[k]:
        k += 1

    if k == l:
        return 'yes'
    else:
        return 'no'


def isequal(l, from1, from2):
    return (
        ((h[from1 + l] + h[from2] * xarr[l]) % p) ==
        ((h[from2 + l] + h[from1] * xarr[l]) % p)
    )


s = input()
q = int(input())

n = len(s)
p = 10 ** 9 + 7
x = 257
h = [0] * (n + 1)
xarr = [0] * (n + 1)
xarr[0] = 1
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x + ord(s[i - 1])) % p
    xarr[i] = (xarr[i - 1] * x) % p

for i in range(q):
    length, a, b = map(int, input().split())
    # print(equal(length, s[a:a+length], s[b:b+length]))
    ans = isequal(length, a, b)
    if ans:
        print('yes')
    else:
        print('no')
