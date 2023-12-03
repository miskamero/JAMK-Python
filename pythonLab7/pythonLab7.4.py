class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}\n"
    
phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)
print(phone1)
print(phone2)