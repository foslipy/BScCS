from threading import Thread,Condition
import time
import random


queue=[]
MAX_num=10
condition=Condition()

class producerthread(Thread):
 def run(self):
    nums=range(5)
    global queue
    while True:
        condition.acquire()
        if len(queue)==MAX_num:
            print("queue full,producer is waiting")
            condition.wait()
            print("space in queue consumer notified the producer")
        num=random.choice(nums)
        queue.append(num)
        print("produced",num)
        condition.notify()
        condition.release()
        time.sleep(random.random())


class consumerthread(Thread):
 def run(self):
    nums=range(5)
    global queue
    while True:
        condition.acquire()
        if not queue:
            print(" nothing in ueue,consumer is waiting")
            condition.wait()
            print("producer added something to ueue and notified the consumer")
        num=random.choice(nums)
        queue.append(num)
        print("consumed",num)
        condition.notify()
        condition.release()
        time.sleep(random.random())



producerthread().start()

consumerthread().start()
()




        
