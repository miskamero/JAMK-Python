nimet = []
def lisaaNimi():
    nimi = str(input("Anna oppilaan nimi: "))
    if nimi != "":
        nimet.append(nimi)
        lisaaNimi()
    else:
        print("Oppilaita:", len(nimet))
        print(*nimet, sep = ", ")

lisaaNimi()