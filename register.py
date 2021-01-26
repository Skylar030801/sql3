import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import *

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='Lifechoicesonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root=tk.Toplevel()
root.title("My logs")
root.geometry("400x400")
root.configure(bg="red")
photo = PhotoImage(file="download.png")
img = Label(root , image=photo)
img.place(x=10, y=0)

lblName = tk.Label(root, text="Please enter Name", )
lblName.place(x=50, y=200)
Name = tk.Entry(root, width=45)
Name.place(x=250, y=200, width=100)
lblSurname = tk.Label(root, text="Please enter Surname ")
lblSurname.place(x=50, y=250)
Surname = tk.Entry(root, width=35)
Surname.place(x=250, y=250, width=100)
lblphone_number = tk.Label(root, text="Please enter phone number ")
lblphone_number.place(x=50, y=300)
phone_number = tk.Entry(root, width=35)
phone_number.place(x=250, y=300, width=100)


def usertable():
    n = Name.get()
    s= Surname.get()
    p = phone_number.get()
    now = datetime.now()
    time= now.strftime("%H:%M %p")
    dt = now.strftime("%d %b %Y")
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='Lifechoicesonline',
                               auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    fmsw = "INSERT INTO register (Name , Surname, phone_number, Time, Date) VALUES(%s ,%s ,%s,%s,%s)"
    try:
        mycursor.execute(fmsw, [(n),(s),(p),(time),(dt)])
        mydb.commit()

        messagebox.showinfo("info","You have successfully registered")

    except:
        messagebox.showinfo("Error", "Please try again")
#if login details are incorrect

def logged():
    d = datetime.now()
    t = d.strftime("%H:%M")
    dt = d.strftime("%d/%m/%y")
    messagebox.showinfo('info', "You have successfully logged in")
    outW = Tk()
    def out():
        d2 = datetime.now()
        t2 = d2.strftime("%H:%M")
        u = Name.get()
        s = Surname.get()
        p = phone_number.get()
        infoU2 = u, s, t, t2, dt, d
        uCom2 = "INSERT INTO register (Name, Surname, Time, phone_number Time_out, Date) VALUES (%s , %s , %s, %s, %s , %s)"

        mycursor.execute(uCom2, infoU2)
        mydb.commit()
        messagebox.showinfo()
    btnOut = Button(outW, text="Out", command=out)
    btnOut.pack()



Registerbtn = tk.Button(root, text="Register new user", bg='Magenta', command=usertable)
Registerbtn.place(x=250, y=350, width=150)



root.mainloop()
