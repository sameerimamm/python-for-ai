class School:
    def __init__(self,s_name):
        self.s_name=s_name

    def teachers(self):
        print("Many teachers")

    def student(self,a):
        print("We have many students but count is :",a)

class Class(School):
    pass

c = Class("ARS")
c.teachers()
c.student(6)