def get_fuel(a, b):
    return round(a * b / 100, 1)
parametri1 = float(input("Anna ajetut kilometrit: "))
parametri2 = float(input("Anna keskikulutus per 100km: "))
print("Bensaa kuluu", get_fuel(parametri1, parametri2), "litraa")

# If param2 is given a decimal number, the program will give a ValueError. This can be fixed by changing the input to float.