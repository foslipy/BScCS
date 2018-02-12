import threading
def fab(nterm):
    n1=0
    n2=1
    count=0
    if nterm<=0:
        print("enter po no")
    elif nterm==1:
        print("fibonaci seunce upto",nterm,":")
        print(n1)
    else:
        
        print("fibonaci seunce upto",nterm,":")        
        while count<nterm:
            print(n1,end=',')
            nth=n1+n2
            n1=n2
            n2=nth
            count +=1
            

if __name__=="__main__":
    nterm=int(input("enter no"))
    t1=threading.Thread(target=fab,args=(nterm,))
    t1.start()
    t1.join()
    print("done")
