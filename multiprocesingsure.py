import multiprocessing
def cal_suare(number,n):
    for i in number:
        n.put(i*i)

if __name__=="__main__":
    number=[8,3,9]
    n=multiprocessing.Queue()
    p=multiprocessing.Process(target=cal_suare,args=(number,n))

    p.start()
    p.join()

    while n.empty() is False:
        print(n.get())
