f = open("17.txt")

a = [int(i) for i in f]

oddmax = 0
oddmin = 10001

for i in a:
    if i % 2 != 0:
        oddmin = min(oddmin, i)
        oddmax = max(oddmax, i)

ans = []
for i in range(len(a) - 1):
    s = a[i] + a[i + 1]
    if s % 2 == 0:
        if s > (oddmax + oddmin):
            ans.append(s)

print(len(ans), min(ans))
