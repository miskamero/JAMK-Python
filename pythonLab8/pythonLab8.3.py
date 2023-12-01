arvosanat = []

def kysymisFunktio():
    try:
        arvosana = int(input("Anna arvosana: "))
        if arvosana < 0 or arvosana > 5:
            raise ValueError
        arvosanat.append(arvosana)
        kysymisFunktio()
    except ValueError:
        KA = sum(arvosanat) / len(arvosanat)
        print("Arvosanojen keskiarvo on", KA)

kysymisFunktio()