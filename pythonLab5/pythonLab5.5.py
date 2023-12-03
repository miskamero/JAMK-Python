def get_cost(ajetutKilometrit, keskiKulutus, litraHinta):
    kulutettuBensiini = ajetutKilometrit * keskiKulutus / 100
    return round(kulutettuBensiini * litraHinta, 2)
parametri1 = int(input("Anna ajetut kilometrit: "))
parametri2 = float(input("Anna kulutus per 100 km: "))
parametri3 = float(input("Anna bensan hinta: "))
print("Bensaa kuluu", get_cost(parametri1, parametri2, parametri3), "euroa")