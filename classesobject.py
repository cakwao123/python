#clss is a blueprint of object
#object is an instant of a class

class Person:
    #properties/attributes/variables/characteristics
    name = "caro"
    age = 20
    gender = "Female"
    #Methods/Function/Behaviour
    def move(self):
        print("Person is walking")
farmer = Person()
farmer.move()
print(farmer.gender)
doctor = Person()