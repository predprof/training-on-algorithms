str1 = input()
str2 = input()

original = {}
for s in str1:
    original[s] = original.get(s, 0) + 1

flag = True
i = 0
while flag and i < len(str2):
    if original.get(str2[i]):
        original[str2[i]] -= 1
    else:
        flag = False
    i += 1

if flag and sum(original.values()) == 0:
    print('YES')
else:
    print('NO')
