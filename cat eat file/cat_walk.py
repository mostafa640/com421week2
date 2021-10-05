class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def walk(self):
        self.weight -= 1

cat1 = Cat("Binnie", 4, 4)
cat2 = Cat("clyde", 1, 2)
cat3 = Cat("tom", 10, 6)
cat1.walk()
cat2.walk()
cat3.walk()
print(cat1.weight)
print(cat2.weight)
print(cat3.weight)