n=int(input('enter no:'))
rev=0
t=n
while(n!=0):
   r=n%10
   n=n//10
   rev=rev+r
if(t==rev):
  print('the no is pallidrom')
else:
  print('the no is not pallidrom')    
