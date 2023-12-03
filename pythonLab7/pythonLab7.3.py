class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def miau(self):
        print(self.name, "Says: Meoooooow!")

Cat1 = Cat("Kit", "Black")
Cat2 = Cat("Kat", "White")

print(Cat1.name + ", " + Cat1.color)
print(Cat2.name + ", " +  Cat2.color)
Cat1.miau()
Cat2.miau()