import threading
def prime():
    f=0
    i=2
    if(n%i==0):
        f=1
    else:
        f=0
    if(f==1):
        print("number is not prime")

    else:
        print("number is prime")

if __name__=="__main__":
    n=int(input("enter no"))
    t1=threading.Thread(target=prime,)
    t1.start()
    t1.join()
    print("done")
