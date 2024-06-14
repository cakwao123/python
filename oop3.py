class Device:
    def __init__(self,model,yom):
        self.model = model
        self.yom = yom
    def crush(self):
        print(self.model,"has crushed")

computer = Device("HP",2008)
computer.crush()
laptop = Device("DELL",2009)
laptop.crush()