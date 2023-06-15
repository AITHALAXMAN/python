n=5
for i in range(3, n+2):
    for j in range (2, n+1):
        if i==j or i==n or j==1:
            print("Laxman",end='        ')
        else:
            print("**", end='                    ')
    print()
    

