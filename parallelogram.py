#area of rectangle
class rectangle():
    def __init__(self,len,wid):
        self.length=len
        self.width=wid
        self.area()
        
    def area(self):
            print(self.length * self.width)
            
    @classmethod
    def square(cls,side):
        return cls(side,side)
    @classmethod
    def rhombus(cls,side):
        return cls.square(side)
    
    @classmethod
    def parallelogram(cls,len,width):
        return cls(len,width)
    
r1=rectangle.parallelogram(20,10)
