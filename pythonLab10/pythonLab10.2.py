# Tee ohjelma joka näyttää onko annettu vuosi karkausvuosi. Vuosiluku kysytään käyttäjältä.

import datetime
pvm = datetime.datetime.now()

def onkoKarkausVuosi(vuosi):
    if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
        return True
    else:
        return False
    
while True:
    try:
        vuosi = int(input("Anna vuosi: "))
        if vuosi < 0:
            print("Vuosi ei voi olla negatiivinen!")
            continue
        elif vuosi > pvm.year:
            print("Vuosi ei voi olla tulevaisuudessa!")
            continue
        else:
            break
    except ValueError:
        print("Virheellinen syöte!")
        continue

if onkoKarkausVuosi(vuosi):
    print(f"Vuosi {vuosi} on karkausvuosi.")
else:
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")
