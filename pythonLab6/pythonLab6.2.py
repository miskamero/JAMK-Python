def celToFah(a):
    return round(a * 1.8 + 32, 1)
def fahToCel(a):
    return round((a - 32) * 5 / 9, 1)

# Select a conversion type
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
valinta = input("Valitse muunnos: ")

if valinta == "1":
    a = float(input("Anna lämpötila: "))
    print(celToFah(a))
elif valinta == "2":
    a = float(input("Anna lämpötila: "))
    print(fahToCel(a))
else:
    print("Virheellinen valinta")