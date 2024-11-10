from tkinter import*
import pymysql
import pymysql.cursors
class employee:
    def getdata(s,b,c,d):
        
         def fun1(self):
             p.set(x)  
         
         win1=Tk()
         x=s.get()
         y=b.get()
         z=c.get()
         a=d.get()
         print(x,y,z,a)
         label=Label(win1,text="id")
         label.grid(row=0,column=0)
         p = StringVar()
         p.set(x)
         tx=Label(win1,text=x)
         tx.grid(row=0,column=1)

         label1=Label(win1,text="name")
         label1.grid(row=1,column=0)
         tx1=Label(win1,text=y)
         tx1.grid(row=1,column=1)
         
         label2=Label(win1,text="address")
         label2.grid(row=2,column=0)
         tx2=Label(win1,text=z)
         tx2.grid(row=2,column=1)
         
         label3=Label(win1,text="salary")
         label3.grid(row=3,column=0)
         tx3=Label(win1,text=a)
         tx3.grid(row=3,column=1)
         #btn = Button(win1,text="sfsdf",command=fun1)
         #btn.grid(row=4,column=1)

    def fun(self):
         pass
         
         
        
"""
def fun():
    user=s.get()
    pasaw=b.get()
    email=c.get()
    cont=d.get()
    con=pymysql.connect(host="localhost",user="root",password="",db="libry")
    try:
        a=con.cursor()
        a.execute("insert into library(username,password,Email_id,contact_number)values('"+user+"','"+pasaw+"','"+email+"','"+cont+"')")
        con.commit()
        print("save")
    except:
        con.rollback()
        print("not save")
    con.close()    
        """

win=Tk()
win.geometry("1368x768")
win.config(bg="grey")
f1=Frame(win,bg="Yellow",height="80",relief=RAISED,bd=10,width=1368)
f1.pack()
head = Label(f1,text="Book Library Management",fg="Pink",bg="white",font=("vendata",45,"bold "),width=1368)
head.pack()
f2 =Frame(win,bg="orange",width="500",height="400",relief="raised",bd="15")
f2.pack(pady=40,side=TOP)
lb=Label(f2,text="registration",fg="pink",bg="white",font=("vendata 30"),justify=CENTER,width=20)
lb.grid(row=0,columnspan=2)
lb1=Label(f2,text="id",font=("vendata 15"),width="10")
s=StringVar()
lb1.grid(row=1,column=0,padx=10,pady=10)
t1= Entry(f2,font=("vendata 13"),textvariable=s)
t1.grid(row=1,column=1)


lb2=Label(f2,text="name",font=("vendata 15"),width="10")
lb2.grid(row=2,column=0,padx=10,pady=10)
b=StringVar()
t2= Entry(f2,font=("vendata 13"),textvariable=b)
t2.grid(row=2,column=1)




lb3=Label(f2,text="address",font=("vendata 15"),width="10")
lb3.grid(row=3,column=0,padx=10,pady=10)
c=StringVar()
t3= Entry(f2,font=("vendata 13"),textvariable=c)
t3.grid(row=3,column=1)




lb4=Label(f2,text="salary",font=("vendata 15"),width="10")
lb4.grid(row=4,column=0,padx=10,pady=10)
d=StringVar()
t4= Entry(f2,font=("vendata 13"),textvariable=d)
t4.grid(row=4,column=1)

btn=Button(f2,text="Submit",fg="pink",font=("vendata 25 bold"),command=lambda:employee.getdata(s,b,c,d),width="10",height="1",padx=10,pady=10,relief="raised",bd="5")
btn.grid(row=5,columnspan=2,padx=10,pady=15)


win.mainloop()
