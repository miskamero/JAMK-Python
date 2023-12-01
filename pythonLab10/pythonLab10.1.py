import datetime
pvm = datetime.datetime.now()

def kerro3(age):
    if age < 1 and age >= 0:
        return "baby"
    elif age < 13:
        return "child"
    elif age >= 13 and age <= 19:
        return "teen"
    elif age >= 20 and age <= 65:
        return "adult"
    else:
        return "senior"
    
while True:
    try:
        syntymaVuosi = int(input("Syntymävuosi: "))
        if syntymaVuosi < 0:
            print("Syntymävuosi ei voi olla negatiivinen!")
            continue
        elif syntymaVuosi > pvm.year:
            print("Syntymävuosi ei voi olla tulevaisuudessa!")
            continue
        else:
            break
    except ValueError:
        print("Virheellinen syöte!")
        continue

age_category = kerro3(pvm.year - syntymaVuosi)
print(age_category)
