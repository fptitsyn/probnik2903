def odd(n):
    s = 0
    for i in range(len(n)):
        if int(n[i]) >= 3:
            return False
        else:
            s += int(n[i])
    if s % 10 == 0:
        return True
    return False


def d(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return len(a)


ans = []
for i in range(1_000_000, 1_222_223):
    b = odd(str(i))
    if b:
        ans.append(i)

for i in range(10, len(ans), 10):
    print(ans[i], d(ans[i]))
