f = open("24.txt")

a = f.readline()

k = 0
kmax = 0
i = 0

while i < len(a) - 2:
    if a[i] in "ABC" and a[i + 1] in "123" and a[i + 2] in "ABC":
        k += 1
        kmax = max(kmax, k)
        i += 2
    else:
        k = 0
    i += 1

print(kmax)