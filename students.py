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


lblName = tk.Label(root, text="Please enter username", )
lblName.place(x=50, y=200)
Name = tk.Entry(root, width=45)
Name.place(x=250, y=200, width=100)
lblSurname = tk.Label(root, text="Please enter password ")
lblSurname.place(x=50, y=250)
Surname = tk.Entry(root, width=35)
Surname.place(x=250, y=250, width=100)
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
        infoU2 = u,s, t, t2, dt
        uCom2 = "INSERT INTO students (Name,Surname, Time, Time_out, Date) VALUES (%s , %s , %s, %s, %s)"

        mycursor.execute(uCom2, infoU2)
        mydb.commit()
        messagebox.showinfo()
    btnOut = Button(outW, text="Out", command=out)
    btnOut.pack()

logbtn = tk.Button(root, text="login", bg='Magenta', command=logged)
logbtn.place(x=250, y=300, width=150)



root.mainloop()
