nimiDictionary = {
}

with open("./nimet.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        if line in nimiDictionary:
            nimiDictionary[line] += 1
        else:
            nimiDictionary[line] = 1
    print(f"Tiedostossa on {len(nimiDictionary)} nimeä.")
    for key, value in nimiDictionary.items():
        print(f"Nimi {key} esiintyy {value} kertaa.")
