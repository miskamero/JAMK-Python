class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # __str__ is a special method that is called when you print an object
        return self.name + " " + str(self.age)
    
Human1 = Human("Adam", 19)
Human2 = Human("Eve", 18)

print(Human1, "\n", Human2)