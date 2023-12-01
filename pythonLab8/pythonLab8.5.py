import random
def lotto():
    lotto = []
    while len(lotto) < 7:
        number = random.randint(1, 40)
        if number not in lotto:
            lotto.append(number)
    lotto.sort()
    return print(*lotto, sep=", ")

lotto()