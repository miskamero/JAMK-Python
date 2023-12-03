def show_cm(a):
    cm = round(a * 2.54, 2)
    return print(a,"tuumaa on ", cm,"senttimetriä")
show_cm(float(input("Anna tuumat: ")))