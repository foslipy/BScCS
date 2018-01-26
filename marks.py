a1=int(input("enter marks for ds"))
a2=int(input("enter marks for .net"))
a3=int(input("enter marks for c"))
a4=int(input("enter marks for python"))
a5=int(input("enter marks for html"))
 

m=a1+a2+a3+a4+a5
print("total marks",m)

avg=a1+a2+a3+a4+a5/5
print("average marks:",avg)

p=(a1+a2+a3+a4+a5)/5
print("percentage:",p)

if(p>=35) & (p<55):
   print("c grade")
elif(p>55) & (p<65):
   print("b grade")
elif(p>65) & (p<85):
   print("A grade")
elif(p>85):
   print("o grade") 
else:
    print("fail")
