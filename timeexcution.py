from time import *
t1= perf_counter()
i, sum = 0, 0
while i<=100000:
    sum+=9
    i+=1
sleep(1+1)
t2 = perf_counter()
print('excution time = %f seconds' %(t2-t1))