class Car:
    def __init__(self,model,color,manufacturer,yop):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.yop = yop

    def speed(self):
        print("the manufacturer of",self.model,"is",self.manufacturer)
car1 = Car("B12","white","BMW",2012)
car1.speed()

car2 = Car("B12","black","MAZDA",2002)
car2.speed()
car3 = Car("B12","red","TOYOTA",2009)
car3.speed()
