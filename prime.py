n=int(input("enter no"))
f=0
for i in range(2,n):
    if (n%i==0):
        f=0
    else:
        f=1
    if(f==1):
        print("no is prime")
    else:
        print("no is not prime")
