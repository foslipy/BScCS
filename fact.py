def fact(number):
    if(number==0):
        return 1
    else:
        return(number*fact(number-1))
n=int(input("enter the number for which you want to find factorial"))
print("the factorial of",n,"is",fact(n))
