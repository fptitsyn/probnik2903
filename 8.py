a = "ЖАЛЕЙ"
c = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    b = a1 + a2 + a3 + a4 + a5
                    if a1 != "Й" and a5 != "Й" and b.count("Й") <= 1:
                        if "ЕЙ" not in b and "ЙЕ" not in b:
                            c += 1

print(c)
