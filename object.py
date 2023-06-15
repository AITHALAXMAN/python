class values():
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
ob=values(10,20)
ob.num3=15
print(ob.num3)
print(hasattr(ob,'num3'))
#has attritude method