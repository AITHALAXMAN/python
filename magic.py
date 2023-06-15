class Magic_check():
    def __init__(self,num):
        self.num=num
    
    def sum(self):
        num=abs(self.num)
        digit_sum=0
        while(num):
            digit_sum += (num%10)
            num //=10
        return digit_sum
    
    def Reverse(self,num):
        rev=0
        while(num):
            rev = rev*10 +(num%10)
            num//=10
        return rev
    
    def Is_Magic(self):
        sod= self.sum()
        rev= self.Reverse(sod)
        prod = sod * rev
        return self.num == prod
num = int(input())
Magic_checker=Magic_check(num)
print(Magic_checker.Is_Magic())
