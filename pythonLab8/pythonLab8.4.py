Dictionary = {
    "ABC-123": "Skoda",
    "DEF-456": "Volvo",
    "GHI-789": "BMW",
    "JKL-012": "Lada",
    "MNO-345": "Audi",
    "PQR-678": "Volkswagen",
    "STU-901": "Toyota",
    "VWX-234": "Saab",
}
print("Kokoelmassa on", len(Dictionary), "Autoa")
while True:
    if len(Dictionary) < 10:
        avain = str(input("Anna auton Rekisterinumero: "))
        arvo = str(input("Anna auton merkki: "))
        Dictionary[avain] = arvo
    else:
        print("Kokoelmassa on 10-autoa, Tulostetaan...")
        for key in sorted(Dictionary.keys()):
            print(key, Dictionary[key])
        break
