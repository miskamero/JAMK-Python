luku = int(input("Anna numero väliltä 1-10: "))
if luku < 1 or luku > 10:
    print("Luku ei ole väliltä 1-10.")
else:
    for i in range (1, luku+1):
        print("Luvun ", i, " neliö on ", i**2)