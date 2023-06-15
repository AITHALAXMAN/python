def happy(num):
    rem=0
    sum=0
    while num>0:
        rem= num%10
        sum+= (rem*rem)
        num//=10
    return sum
num = 978
r=num
while r!=1 and r!=4:
    r=happy(r)
if r==1:
    print("happy number")
else:
    print("unhappy")