ftr=input("Enter file name to be copy:")
f1=open(ftr,'r')
rd=f1.read()

ftw=input("enter file nameto be paste:")
f2=open(ftw,'w')
f2.write(rd)
f1.close()
f2.close()
