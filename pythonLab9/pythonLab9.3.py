with open('luvut.txt', 'w') as lukuTiedosto:
    counter = 0
    while True:
        if lukuTiedosto.writable():
            luku = input('Syötä Luku: ')
            if len(luku) > 0:
                lukuTiedosto.write(luku)
                lukuTiedosto.write('\n')
                counter += 1
            if len(luku) <= 0:
                    print(f"Tiedostossa on {counter} lukua.")
                    break
        else:
            print('Tiedosto ei ole kirjoitettavissa.')
            break