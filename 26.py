f = open("26.txt")

a = [int(i) for i in f][1:]
a = sorted(a, reverse=True)

s1 = 0
s2 = 0

for i in range(len(a)):
    if i < len(a) // 4:
        s1 += a[i] / 2
    else:
        s1 += a[i]
    if i >= 7500:
        s2 += a[i] / 2
    else:
        s2 += a[i]

print(s1, s2)
