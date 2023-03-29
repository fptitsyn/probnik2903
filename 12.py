for n in range(1, 100):
    s = "1" * 15 + "2" * n
    while "12" in s:
        s = s.replace("12", "4", 1)
    s1 = sum([int(i) for i in s])
    if s1 == 48:
        print(n, s)