#To show how a class method falls of function which is defined in the global name space of a program ?

def measure(y):
    return y*1000
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var=", self.var)
    def modify(self):
        self.var= measure(self.var)
obj=abc(100)
obj.display()
obj.modify()
obj.display()