import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

root=Tk()
root.title("My logs")
root.geometry("950x400")
root.configure(bg="red")


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='Lifechoicesonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Visitors")
results = mycursor.fetchall()
i = 0
if results:
    for x in results:
        for v in range(len(x)):
            print(x[v])
            e = tk.Entry(root, width=20)
            e.grid(row=i, column=v)
            e.insert(END, x[v])
        i=i+1


mycursor.execute("SELECT * FROM admin")
results = mycursor.fetchall()
i = 0
if results:
    for x in results:
        for v in range(len(x)):
            print(x[v])
            e = tk.Entry(root, width=20)
            e.grid(row=i, column=v)
            e.insert(END, x[v])
        i=i+1

mycursor.execute("SELECT * FROM staff")
results = mycursor.fetchall()
i = 0
if results:
    for x in results:
        for v in range(len(x)):
            print(x[v])
            e = tk.Entry(root, width=20)
            e.grid(row=i, column=v)
            e.insert(END, x[v])
        i=i+1

results = mycursor.execute("SELECT * FROM register")

i = 0
if results:
    for x in results:
        for v in range(len(x)):
            print(x[v])
            e = tk.Entry(root, width=20)
            e.grid(row=i, column=v)
            e.insert('end', x[v])
        i=i+1


def close():
    exit = messagebox.askyesno(title="?", message="do you want to exit?")
    if exit ==True:
        root.destroy()
    else:
        return None

def clear():
    mycursor.execute("TRUNCATE TABLE register")
    messagebox.showinfo("DELETE", "ALL register User Deleted")
    root.destroy()

exitbtn = tk.Button(root, command=close, bg="pink", text="exit")
exitbtn.place(x=230, y=150)

clearbtn = tk.Button(root, command=clear, bg="pink", text="clear")
clearbtn.place(x=230, y=200)







root.mainloop()
