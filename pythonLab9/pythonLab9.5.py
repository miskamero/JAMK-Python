import random

def lotto():
    rivit = int(input("Luotavat rivit: "))
    try:
        lottoTiedosto = open("./lotto.txt", "w")  # Open the file outside the loop
        for i in range(1, rivit+1):
            lotto = []
            while len(lotto) < 7:
                number = random.randint(1, 40)
                if number not in lotto:
                    lotto.append(number)
            lotto.sort()
            lottoString = ", ".join(str(num) for num in lotto)
            lottoTiedosto.write(lottoString + "\n")  # Write each lotto row to a new line
            print(f"Rivi {i}: {lottoString}")
        lottoTiedosto.close()  # Close the file after the loop
    except Exception as e:
        print(f"Virhe lotto{i}.txt tiedostoa luodessa:", str(e))

lotto()
