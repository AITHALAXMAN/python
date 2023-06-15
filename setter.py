# using property and setter

class sample:
    def __init__(self,val):
        self.val=val
    @property
    def val(self):
        return self.__val
    @val.setter
    def val(self,val):
        self.__val=val
s=sample(20)