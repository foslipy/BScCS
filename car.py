import tkinter
from tkinter import *
root=Tk()
# mian background
c=Canvas(root,bg="white",width=800,height=600,)
#second wagon
c.create_rectangle(350,200,200,250,fill="red")
c.create_oval(200,200,250,280,fill="black")
c.create_oval(350,200,300,280,fill="black")
c.create_rectangle(350,120,200,200,fill="brown")
c.create_rectangle(270,165,210,200,fill="white")
c.create_rectangle(350,165,300,200,fill="white")
#first wagon
c.create_line(0,280,800,280,fill="black",width=5)
c.create_rectangle(600,200,400,250,fill="blue")
c.create_oval(400,200,450,280,fill="black")
c.create_oval(600,200,550,280,fill="black")
c.create_rectangle(520,120,410,200,fill="brown")
c.create_rectangle(590,150,520,200,fill="yellow")
c.create_rectangle(580,170,550,200,fill="white")
c.create_line(350,230,400,230,fill="black",width=10)
#exausts
c. create_rectangle(570,100,550,150,fill="black")
c.pack()
