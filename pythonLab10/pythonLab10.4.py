nimiTiedosto = open("./names.txt", "r", encoding="utf-8")
nimiLista = []

try:
    for nimi in nimiTiedosto:
        nimiLista.append(nimi.strip())
    print(f"Tiedostossa on {len(nimiLista)} nimeä.")
    print(f"Pisin nimi on {max(nimiLista, key=len)}.")
except Exception as e:
    print(f"Virhe: {e}")
finally:
    nimiTiedosto.close()
