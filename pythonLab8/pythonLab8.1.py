nimet = []
i = int(1)
while i <= 10:
    nimi = input("Anna nimi: ")
    nimet.append(nimi)
    i += 1

print(*nimet, sep=", ")
nimet.reverse()
print(*nimet, sep=", ")