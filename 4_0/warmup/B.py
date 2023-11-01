def nod(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


a, b, c, d = map(int, input().split())

if b == d:
    m = a + c
    n = b
else:
    m = a * d + b * c
    n = b * d

get_nod = nod(m, n)
print(m // get_nod, n // get_nod)
