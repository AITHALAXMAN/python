class val():
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
        self.division()
    def division(self):
        print(self.num1/self.num2)
        
    @classmethod
    def trial(cls,n1,n2):
        if(n1>n2):
           return cls(n1,n2)
        else:
            return cls(n2,n1)
      
nu1=int(input("enter n1 value:"))
nu2=int(input("enter n2 value:"))
v1=val.trial(nu1,nu2)