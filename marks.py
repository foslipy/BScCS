sname=input('enter name')
m1=int(input('enter marks of subject 1'))
m2=int(input('enter marks of subject 2'))
m3=int(input('enter marks of subject 3'))
m4=int(input('enter marks of subject 4'))
m5=int(input('enter marks of subject 5'))
m6=int(input('enter marks of subject 6'))
total=m1+m2+m3+m4+m5+m6
per=total/6
print('name',sname)
print('total marks',total)
print('percentage=',format(per,'.2f'),'%')

