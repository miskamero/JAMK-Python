class Account:
    def __init__(self, saldo):
        self.saldo = saldo

    def withdraw(self, money):
        money = abs(money)
        if money <= self.saldo:
            self.saldo -= money
            return self.saldo
        else:
            print("Virheellinen summa!")

    def add(self, money):
        money = abs(money)
        self.saldo += money
        return self.saldo

    def __str__(self):
        return f"Saldo on {self.saldo} euroa."
    
Account1 = Account(2000)

while True:
    try:
        print(f"Saldo: {Account1.saldo} euroa")
        print("1) Nosta rahaa")
        print("2) Talleta rahaa")
        print("3) Lopeta")
        valinta = int(input("Valinta: "))
        if valinta == 1:
            raha = int(input("Nostettava summa: "))
            Account1.withdraw(raha)
        elif valinta == 2:
            raha = int(input("Talletettava summa: "))
            Account1.add(raha)
        elif valinta == 3:
            break
        else:
            print("Valitse 1-3!")
            continue
    except ValueError:
        print("Virheellinen syöte!")
        continue