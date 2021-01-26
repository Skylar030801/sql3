import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image

root=tk.Toplevel()
root.title("My logs")
root.geometry("600x600")
root.configure(bg="red")
photo = PhotoImage(file="download.png")
img = Label(root , image=photo)
img.place(x=10, y=0)


lbluser = tk.Label(root, text="Please enter username", )
lbluser.place(x=50, y=200)
Username = tk.Entry(root, width=45)
Username.place(x=250, y=200, width=100)
lblpassword = tk.Label(root, text="Please enter password ")
lblpassword.place(x=50, y=250)
Password = tk.Entry(root, width=35)
Password.place(x=250, y=250, width=100)
Password.config(width=20, show='*')


def admin_Login():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='Lifechoicesonline',
                               auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    users = Username.get()
    passs = Password.get()
    sql = "select * from admin where Username = %s and Password = %s"
    mycursor.execute(sql, [(users), (passs)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            messagebox.showinfo("SUCCESS")
            import admin_thing

            break

    else:
        messagebox.showerror("ERROR")


admin_btn = Button(root, text="SIGN-IN",bg='Magenta' , width=20, command=admin_Login)
admin_btn.place(x=100, y=300)
root.mainloop()
