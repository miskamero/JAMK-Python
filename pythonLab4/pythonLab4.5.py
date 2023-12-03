etuNimi = str(input("Anna etunimesi: "))
sukuNimi = str(input("Anna sukunimesi: "))
etuNimiShenanigans = etuNimi[0] * len(etuNimi)
sukuNimiShenanigans = sukuNimi[::-1]
print(etuNimiShenanigans, sukuNimiShenanigans)