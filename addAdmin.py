from tkinter import*

from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="lifechoices1",
  password="@Lifechoices1234",
	database="lifechoicesonline", auth_plugin='mysql_native_password'
)

root = Tk()
root.geometry('600x400')
root.title("Registration Form")
registrationLabel = Label(root, text="Add admin form",width=20,font=("bold", 20))
registrationLabel.place(x=150,y=53)

# Labels

username_lbl = Label(root, text="Username:",width=20,font=("bold", 10))
username_lbl.place(x=80,y=150)
password_lbl = Label(root, text="Password:",width=20,font=("bold", 10))
password_lbl.place(x=80,y=200)

# Entries
username_entry = Entry(root)
username_entry.place(x=240,y=150)
password_entry = Entry(root)
password_entry.place(x=240,y=200)

mycursor = mydb.cursor()
def register_user():
    user_name = username_entry.get()
    pass_word = password_entry.get()
    try:
        sql = "INSERT INTO Admin VALUES (%s,%s )"
        mycursor.execute(sql, [user_name, pass_word])
        result = mycursor.fetchone()
        mydb.commit()
        messagebox.showinfo("INSERTION", "Admin Inserted")
    except:
        messagebox.showinfo("INSERTION", "Admin Insertion failed")


insert_btn=Button(root,command=register_user, text='Insert',width=20,bg='blue',fg='white').place(x=220,y=250)



def exit():
    root.destroy()

btnExit=Button(root, text="Quit", command=exit, width=20,bg='blue',fg='white')
btnExit.place(x=220,y=280)
root.mainloop()

