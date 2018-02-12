fn=input("enter file name:")
f1=open(fn,'r')
r=f1.read()
l=len(r)
print("no of char:",l)
print(r)

i=1
   
w=len(r.split())
print("word in line",w)
f1.close()
