eurot = int(input("Eurojesi määrä: "))
sentit = int(input("Senttieis määrä: "))
print("Euroja: ", eurot)
print("Senttejä: ", sentit)
aidotSentit = sentit / 100
rahaYht = eurot + aidotSentit
print("Sinulla on: ", rahaYht)