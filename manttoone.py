class A():
    num1 = 10
    pass
class B():
    num2=20
        
class C(A,B):
    num3=30
    
class D(C,A,B):
    pass

print(C.num3)
    
