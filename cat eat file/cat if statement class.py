class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def walk(self):
      if self.weight<=1:
        print("cat can not walk")
      else:
        self.weight -= 1

catobject1 = Cat("Binnie", 4, 4)
catobject2 = Cat("Clyde",1 , 2)
catobject3 = Cat("Tom", 10, 6)

print("weight before walking")


print(catobject1.weight)
print(catobject2.weight)
print(catobject3.weight)

catobject1.walk()
catobject2.walk()
catobject3.walk()

print("weight after walking")

print(catobject1.weight)
print(catobject2.weight)
print(catobject3.weight)

catobject1.walk()
catobject2.walk()
catobject3.walk()

print("weight after walking")
catobject1.walk()
catobject2.walk()
catobject3.walk()