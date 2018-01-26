import tkinter
from tkinter import*
cal=Tk()
cal.title("calculator")
operator=""
text_input =StringVar()

dispalay=Entry(cal,font=('arial',30,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="purple",justify='right').grid(columnspan=5)
#1st line
b7=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="7").grid(row=1,column=0)
b8=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="8").grid(row=1,column=1)
b9=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="9").grid(row=1,column=2)
ADD=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="+").grid(row=1,column=3)

#2nd line
b4=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="4").grid(row=2,column=0)
b5=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="5").grid(row=2,column=1)
b6=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="6").grid(row=2,column=2)
SUB=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="_").grid(row=2,column=3)

#3rd line
b1=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="1").grid(row=3,column=0)
b2=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="2").grid(row=3,column=1)
b3=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="3").grid(row=3,column=2)
MUL=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="*").grid(row=3,column=3)

#4th line
bclear=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="C").grid(row=4,column=0)
b0=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="0").grid(row=4,column=1)
bequal=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="=").grid(row=4,column=2)
DIV=Button(cal,padx=20,pady=20,bd=10,fg="black",font=('arial',20,'bold'),text="/").grid(row=4,column=3)


cal.mainloop()
