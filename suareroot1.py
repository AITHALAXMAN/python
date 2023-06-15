class Square_Root:
    def __init__(self,num):
        self.num=num
    def SqRoot(self):
        for i in range(1,self.num):
            if i*i==self.num:
                return i
n=int(input())
s=Square_Root(n)
print(s.SqRoot())