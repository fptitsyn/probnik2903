def f(x, y, s):
    if x == y and s[-2] == "2":
        return 1
    if x > y:
        return 0
    return f(x + 1, y, s + "1") + f(x + 2, y, s + "2")

print(f(3, 18, ""))