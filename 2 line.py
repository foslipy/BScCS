import tkinter
from tkinter import*
root=Tk()
c=Canvas(root,height=500,width=900,bg="yellow")
c.create_line(250,250,650,150,fill='black')
c.create_line(250,250,650,300,fill='black')
c.pack()
root.mainloop()
