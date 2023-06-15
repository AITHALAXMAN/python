# composition of multipath
class one:
    def set(self,var):
        self.var=var
    def get(self):
        return self.var
        
class two:
    def __init__(self, var):
        self.o= one()
        self.o.set(var)
    def show(self):
        print("number= ", self.o.get())
        
t= two(100)
t.show()