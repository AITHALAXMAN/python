#Q)write a parent class of a person to take name and age of a person ?

class parent():
    def __intit__(self,name,age):
        self.name=name
        self.age=age
    def __display(self):

class teacher():
    def __init__(self,name,age,designation,exp):
        person.__init__(self,name,age)
        self.name=name
        self.age=age
        self.designation=designation
        self.exp=exp
    def __display(self):
        print(self.name)
        print(self.age)
        print(self.designation)
        print(self.exp)
        self.display
        
        
class student():
    def __init__(self,name,age,branch,year):
        person.__init__(self,name,age)
        self.branch=branch
        self.year=year
        
teach1=teacher('laxman',21,'ceo',5)