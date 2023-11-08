def z_func(string, length):
    z = [0] * length
    left, right = 0, 0
    for i in range(1, length):
        z[i] = max(0, min(right - i, z[i - left]))
        while i + z[i] < length and string[z[i]] == string[i + z[i]]:
            z[i] += 1

        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z


s = input()
n = len(s)
print(*z_func(s, n))
