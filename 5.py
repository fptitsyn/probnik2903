def f(n):
    if n % 2 == 0:
        n //= 2
    else:
        n -= 1
    if n % 3 == 0:
        n //= 3
    else:
        n -= 1
    if n % 5 == 0:
        n //= 5
    else:
        n -= 1
    return n

c = 0
for n in range(1, 100000):
    if f(n) == 3:
        print(n)
        c += 1

print(c)