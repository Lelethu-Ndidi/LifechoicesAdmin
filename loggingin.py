from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="lifechoices1",
    password="@Lifechoices1234",
    database="lifechoicesonline", auth_plugin='mysql_native_password'
)

login_screen = Tk()
login_screen.title("Log in")
login_screen.geometry("300x250")

# Set text variables
username = StringVar()
password = StringVar()

# Set label for user's instruction
instruction = Label(login_screen, text="   Please enter your username and password:   ", bg="blue").pack()
Label(login_screen, text="").pack()

# Set username label
username_label = Label(login_screen, text="Username * ")
username_label.pack()

# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

username_entry = Entry(login_screen, textvariable=username)
username_entry.pack()

# Set password label
password_label = Label(login_screen, text="Password * ")
password_label.pack()

# Set password entry
password_entry = Entry(login_screen, textvariable=password, show='*')
password_entry.pack()

Label(login_screen, text="").pack()

mycursor = mydb.cursor()

# Checking if the entered data is the same as the data on the database if yes, you are logged in
def verify():
    user_verification = username_entry.get()
    pass_verification = password_entry.get()
    sql = "select * from Login where Username= %s and Password =%s"
    mycursor.execute(sql, [user_verification, pass_verification])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

# message box displayig you are logged in
def logged():
    messagebox.showinfo("LOG MESSAGE", "You have successfully logged in")
    login_screen.withdraw()
    import options

# message box displaying you failed to log in
def failed():
    messagebox.showinfo("LOG MESSAGE", "Username or password is incorrect")
    username_entry.delete(0, END)
    password_entry.delete(0, END)


# Set login button
Button(login_screen, command=verify, text="Login", width=10, height=1, bg="blue").pack()


def exit():
    login_screen.destroy()


Button(text="Quit", command=exit, width=5, height=1, bg='blue', fg='white').pack()

login_screen.mainloop()  # start the GUI
