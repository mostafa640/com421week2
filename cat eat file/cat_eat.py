class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        self.weight += 1

cat1 = Cat("Binnie", 4, 4)
cat2 = Cat("Clyde", 1, 2)
print("weight before eating")
print(cat1.weight)
print(cat2.weight)

print("weight after eating")
cat1.eat()
print(cat1.weight)
cat2.eat()
print(cat2.weight)