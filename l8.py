# Q) write a python program tao take student name student marks as a list and return their average ?

        
class students:
    count = 0
    def __init__(self, name):
        self.name = name
        self.marks = []
        students.count = students.count + 1
        
    def enterMarks(self):
        for i in range(3):
            m = int(input("Enter the marks of %s in %d subject: "%(self.name, i+1)))
            self.marks.append(m)
            
    def display(self):
        print (self.name, "got ", self.marks)
    def avrg(self):
        avg=sum(self.marks)/len(self.marks)
        print(avg)
    def display(self):
        print(self,name, self.marks)
             
name = input("Enter the name of Student:")
s1 = students(name)
s1.enterMarks()
s1.display()
print (" ")
    
