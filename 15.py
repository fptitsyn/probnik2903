def d(x, y):
    return x % y == 0


ans = []
for a in range(1, 1000):
    for x in range(1, 1000):
        if not ((d(120, a)) and ((not d(x, a)) <= ((d(x, 36)) <= (not d(x, 15))))):
            break
    else:
        ans.append(a)

print(max(ans))