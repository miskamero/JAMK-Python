piste1 = int(input("Hypyn pisteet: "))
piste2 = int(input("Hypyn pisteet: "))
piste3 = int(input("Hypyn pisteet: "))
piste4 = int(input("Hypyn pisteet: "))
piste5 = int(input("Hypyn pisteet: "))

pisteet = [piste1, piste2, piste3, piste4, piste5]
pisteet.sort()
pisteet.pop(0)
pisteet.pop(-1)
print("Pisteet yhteensä: ", sum(pisteet))