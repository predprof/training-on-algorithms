s = input()

ans = ''
open_b = []
d = {
    ')': '(',
    ']': '[',
    '}': '{',
}

count = {
    '(': 0,
    '[': 0,
    '{': 0,
}

for i in s:
    if i in ['(', '[', '{']:
        open_b.append(i)
        count[i] += 1
    elif len(open_b) == 0:
        ans = 'no'
        break
    else:
        if open_b[-1] == d[i]:
            count[d[i]] -= 1
            open_b.pop()
        else:
            ans = 'no'
            break

if not ans and sum(count.values()) == 0:
    ans = 'yes'
else:
    ans = 'no'

print(ans)
