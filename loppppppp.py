class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def prepending(self,data):
           newnode=Node(data)
           if self.head==None:
              self.head=newnode
              self.tail=newnode
           else:
              newnode.next=self.head
              self.head=newnode
           print("newnode inserted at the head postion")
           self.size+=1
x=Linkedlist()
value=int(input("enetr the value to be inserted"))
x.prepending()

print(value)
