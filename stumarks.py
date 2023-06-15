class info():
    def __init__(self,name):
        self.name=name
        self.marks= []
        self.get_marks()
        self.avrg()
        self.display()
    def get_marks(self):
        for i in range (1,7):
            m = int(input("enter marks"))
            self.marks.append(m)
    def avrg(self):
        avg=sum(self.marks)/len(self.marks)
        print(avg)
    def display(self):
        print(self,name, self.marks)
    
            