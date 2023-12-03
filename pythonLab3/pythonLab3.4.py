pisteet = int(input("Anna pisteesi: "))
if pisteet < 0 or pisteet > 12:
    print("Epäkelpo pistemäärä")
elif pisteet == 0 or pisteet == 1:
    print("Arvosana: 0")
elif pisteet == 2 or pisteet == 3:
    print("Arvosana: 1")
elif pisteet == 4 or pisteet == 5:
    print("Arvosana: 2")
elif pisteet == 6 or pisteet == 7:
    print("Arvosana: 3")
elif pisteet == 8 or pisteet == 9:
    print("Arvosana: 4")
elif pisteet >= 10:
    print("Arvosana: 5")