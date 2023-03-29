f = open("27a.txt")

summa = 0
min_disc = 100000000000000
min2 = 1000000000000000000
min3 = 1000000000000000000

for s in f:
    a = sorted([int(i) for i in s.split()], reverse=True)
    print(a)
    if len(a) == 3:
        summa += a[0] + a[1]
        if a[1] - a[2] < min_disc:
            min_disc = a[1] - a[2]
            min2 = a[1]
            min3 = a[2]

if summa % 5 != 0:
    print(summa)
else:
    print(summa - min_disc)
