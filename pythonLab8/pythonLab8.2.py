rekkarit = []
def järjestysFunktio():
    rekkarit.sort()
    print(*rekkarit, sep = ", ")
def lisääRekkari():
    rekkari = input("Anna rekkari (7-merkkiä): ")
    if rekkari == "":
        järjestysFunktio()
    elif rekkari in rekkarit:
        print("Rekkari on jo listalla!")
        lisääRekkari()
    elif len(rekkari) != 7:
        print("Rekkari on väärän mittainen!")
        lisääRekkari()
    else:
        rekkarit.append(rekkari)
        lisääRekkari()

lisääRekkari()
