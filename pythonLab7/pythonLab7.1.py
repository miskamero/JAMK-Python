class Pelikortti:
    def __init__(self, maa, arvo):
        self.maa = maa
        self.arvo = arvo

kortti1 = Pelikortti("Hertta", 10)
kortti2 = Pelikortti("Ruutu", 2)
kortti3 = Pelikortti("Pata", 14)
kortti4 = Pelikortti("Risti", 7)
kortti5 = Pelikortti("Risti", 2)

print(kortti1.maa, kortti1.arvo)
print(kortti2.maa, kortti2.arvo)
print(kortti3.maa, kortti3.arvo)
print(kortti4.maa, kortti4.arvo)
print(kortti5.maa, kortti5.arvo)