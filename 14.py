def f(x, q):
    a = ""
    while x > 0:
        a += str((x % q))
        x //= q
    return a


d = (729**41 - 81 ** 16) * (729**15 + 9 ** 5)
print(f(d, 9).count("8"))
