with open('sukunimet.txt', 'w') as nimiTiedosto:
    while True:
        if nimiTiedosto.writable():
            sukunimi = input('Anna sukunimesi: ')
            if len(sukunimi) > 0:
                nimiTiedosto.write(sukunimi)
                nimiTiedosto.write('\n')
            if len(sukunimi) <= 0:
                print('Tiedosto suljetaan.')
                break
        else:
            print('Tiedosto ei ole kirjoitettavissa.')
            break