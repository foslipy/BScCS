class Node :
    def __init__(self,data):
        self.data=data




        self.next=None
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
        
        
    def insertfromtail(self,data):
        newnode=node(data)
        if self.tail==None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        print("newnode inserted at the tail postion")
        self.size+=1
        
    def deletefromhead(self):
        if self.head==None:
            print("linkedlist is empty")
        else:
            current=self.head
            while(current.next!=None):
                prev=current
                current=current.next
            value=current.data
            prev.next=None
            print("deleted node is:",value)
            self.tail=prev
            self.size-=1

    def traversalofLL(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
        print("end")

    def search(self,value):
        self.n=0
        current=self.head
        while(current!=None):
            self.n+=1
            if current.data!=value:
                current=current.next
            else:
                return True
        return False

    def deletevalue(self,value):
        current=self.head
        while(current!=None and current.data!=value):
            prev=current
            current=current.next
        if current==None:
            print("node not found")
        else:
            self.size-=1
            if current==self.head:
                self.head=current.next
            elif current==self.tail:
                prev.next=current.next
                self.tail=prev
            else:
                prev.next=current.next
            print("value deleted succesfully")
x=Linkedlist()
print("menu")
print("1.prepand \n2.Insert from tail \n3.delete from head \n4.delete from tail")
print("5.search for a value \n6.delete a value \n7.display linkedlist \n8.exit")
choice=int(input("pls enter choice"))
while(choice!=8):
    if choice==1:
        value=int(input("enetr the value to be inserted"))
        x.prepending(value)
    if choice==2:
        value=int(input("enter the value to be inserted"))
        x.insertfromtail(value)
    if choice==3:
        x.deletefromhead()
    if choice==4:
        x.deletefromtail(value)
    if choice==5:
        value=int(input("enter the value to be delelted"))
        x.deletevalue(value)
    if choice==7:
        x.traversalofLL(value)
    choice=int(input("enter your choice again"))
        
        
    
        
