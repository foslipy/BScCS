import threading
def add(n):
    a=0
    while(n>=1):
        m=int(input("enter no:"))
        if(m>=0):
            a=a+m
        else:
            print("number is negative")
            n=n-1

if __name__=="__main__" :
    n=int(input("enter range"))
    t1=threading.Thread(target=add ,args=(n,))
    t1.start()
    t1.join()
    print("done")
    
