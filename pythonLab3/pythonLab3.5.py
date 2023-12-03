luku1 = int(input("Anna 1. luku: "))
luku2 = int(input("Anna 2. luku: "))
luku3 = int(input("Anna 3. luku: "))
luku4 = int(input("Anna 4. luku: "))
luku5 = int(input("Anna 5. luku: "))
luvut = int(0)
if luku1 > 0:
    luvut += luku1
if luku2 > 0:
    luvut += luku2
if luku3 > 0:
    luvut += luku3
if luku4 > 0:
    luvut += luku4
if luku5 > 0:
    luvut += luku5
print("Lukujen summa: ", luvut)
