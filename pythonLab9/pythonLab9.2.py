with open("./sukunimet.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    print(*lines, sep="\n")
    lines.sort()
    print("Sukunimet aakkosjärjestyksessä:")
    print(*lines, sep="\n")