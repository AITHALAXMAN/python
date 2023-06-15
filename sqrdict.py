class Square_Root:
    def __init__(self,num):
        self.num=num
s=Square_Root(10)
print(s.__dict__)
s.Laxman=6
print(s.__dict__)
del s.num
print(s.__dict__)