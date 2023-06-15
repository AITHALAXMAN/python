# program to use get and set functions to retrive and set a value

class sample:
    def __init__(self,val):
        self.val = val
    def get_val(self):
        return self.val
    def set_val(self,val):
        self.val=val
s=sample(20)
s.set_val(30)
print(s.get_val())
