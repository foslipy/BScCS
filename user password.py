import tkinter
from tkinter import*
from tkinter import messagebox
root=Tk()
def welc():
        u=str(e1.get())
        p=str(e2.get())
        if p=="admin":
           n="welcome admin"
           messagebox.showinfo("message",n)
        else:
            n1="welcome"
            messagebox.showinfo("message",n1)

l=Label(root,text="login page")
l.grid(row=0,column=1)

l1=Label(root,text='user name')
l1.grid(row=1,column=0)
e1=Entry(root,relief="sunken",bd=2)
e1.grid(row=1,column=2)

l2=Label(root,text="password")
l2.grid(row=2,column=0)
e2=Entry(root,relief="sunken",bd=2,show='$')
e2.grid(row=2,column=2)
b=Button(root,text="login",relief="raised",bd=2,command=welc)
b.grid(row=3,column=1)
root.mainloop()
