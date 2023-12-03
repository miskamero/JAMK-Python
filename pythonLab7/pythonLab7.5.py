class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def __str__(self):
        return f"{self.brand} {self.model} {self.price}"

auto1 = Car(brand="Skoda", model="Octavia", price=3000)
auto2 = Car(brand="Audi", model="A4", price=4000)
auto3 = Car(brand="Volvo", model="V70", price=5000)

print(auto1)
print(auto2)
print(auto3)
print("Autojen hinta yhteensä: ", auto1.price + auto2.price + auto3.price)