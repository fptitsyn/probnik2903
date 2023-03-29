def f(s1, s2, c, m):
    if s1 + s2 >= 47:
        if s1 + s2 <= 59:
            return c % 2 == m % 2
        else:
            return (c + 1) % 2 == m % 2
    if c > m:
        return 0
    a = [f(s1 + 2, s2, c + 1, m), f(s1 * 3, s2, c + 1, m), f(s1, s2 + 2, c + 1, m), f(s1, s2 * 3, c + 1, m)]
    if (c + 1) % 2 == m % 2:
        return any(a)
    else:
        return all(a)


c2 = 0
c4 = 0
s1 = 5
for s2 in range(1, 42):
    for m in range(1, 8):
        if f(s1, s2, 0, m):
            print(s2, m)
            break
