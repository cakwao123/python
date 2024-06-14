#Parent class/Base class/Super class
class Animal:
    hasscales = True
    def sound (self):
        print("Animal is speaking")
#class inheriting from another
class Duck(Animal):
    haswings = True
    def move (self):
        print("Duck is swimming")

class Caterpillar:
    def move (self):
        print("Caterpillar is slittering")
a =Animal()

d = Duck()
print(d.haswings)
c =Caterpillar()
