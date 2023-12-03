def showtime(s):
    tunnit, remainder = divmod(s, 3600)
    minuutit, sekunnit = divmod(remainder, 60)
    roundedTunnit = round(tunnit)
    roundedMinuutit = round(minuutit)
    roundedSekunnit = round(sekunnit)
    if roundedTunnit < 10:
        roundedTunnit = "0" + str(roundedTunnit)
    if roundedMinuutit < 10:
        roundedMinuutit = "0" + str(roundedMinuutit)
    return str(roundedTunnit) + ":" + str(roundedMinuutit) + ":" + str(roundedSekunnit)

sekunnit = float(input("Anna sekunnit: "))
print(showtime(sekunnit))