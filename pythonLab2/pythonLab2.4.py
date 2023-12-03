import datetime
nimi = str(input("Anna Etunimesi: "))
syntymaVuosi = int(input("Anna Syntymävuotesi: "))
vuosiNyt = int(datetime.datetime.now().year)
ika = vuosiNyt - syntymaVuosi
print("Hei ", nimi, ", olet ", ika, " vuotta.")