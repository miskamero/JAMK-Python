luvut = []
while True:
    try:
        luku = int(input("Anna luku: "))
    except ValueError:
        print("Lukuja annettu: ", len(luvut))
        print("Lukujen summa: ", sum(luvut))
        break
    else:
        luvut.append(luku)