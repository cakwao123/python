class Students:
    def __init__(self,firstname,course,gender):
        self.firstname = firstname
        self.course = course
        self.gender = gender
    def study (self):
        print(self.firstname,"is studyng")

student1 = Students("Caro","MIT","female")
student1.study()
student2 = Students("jane","DATASCIENCE","female")
student2.study()
student3 = Students("joy","CYBER SECURITY","female")
student3.study()