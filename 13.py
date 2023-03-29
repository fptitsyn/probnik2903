s = "АВ БАД ВБЕ ГБВД ДЗ ЕЖ ЖГК ЗГЖ КЗ"
p = {x[0]: x[1:] for x in s.split()}


def f(s, e):
    if e == s[-1] and len(s) > 1:
        return 1
    return sum([f(s + c, e) for c in p[s[-1]] if c not in s[1:]])


print(f("Г", "Г"))
