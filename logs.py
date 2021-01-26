import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk




mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='Lifechoicesonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
def verify():
    users = Username.get()
    passs = Password.get()
    sql = "select * from Login where username = %s and password = %s"
    mycursor.execute(sql, [(users), (passs)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("result", "You have successfully logged")
        root.withdraw()
        import mainmenu
        mainmenu.mainloop()


    else:
        failed()




def failed():
    messagebox.showinfo("Error, try again")
    Username.delete(0, END)
    Password.delete(0, END)

#Design the login form
root = tk.Tk()
root.geometry("400x400")
root.title("Login Page")
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

Loginbtn = tk.Button(root, text="Login", bg='Magenta', command=verify)
Loginbtn.place(x=150, y=300, width=55)





root.mainloop()
