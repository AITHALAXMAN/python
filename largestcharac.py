# Q) Write a program to use a constructor to build an array of characters and Find the largest in three inputs?
class number:
    def __init__(self):
        self.values= []
    def find_max(self):
        max= " "
        for i in self.values:
            if i>max:
                max=i
        print("max= %r" %max)
    def insert_element(self):
        value=input('enter element')
        self.values.append(value)
x=number()
ch='y'
while ch=='y':
    x.insert_element()
    ch= input("do u wish to enter more elements")
x.find_max()