# Imports
from tkinter import *
import mysql.connector

# Database Connection with python
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="lifechoices1",
  password="@Lifechoices1234",
	database="lifechoicesonline", auth_plugin='mysql_native_password'
)

# Creating a window
main_screen = Tk()   # create a GUI window
main_screen.geometry("300x250") # set the configuration of GUI window
main_screen.title("Account Login") # set the title of GUI window

# create a Form label
Label(text="Press the button to log in", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

# Function Login, You click the button to go to the next page which is a login page
def login():
    main_screen.withdraw()
    import loggingin

# create Login Button
loginbtn=Button(text="Login", command=login,height="2", width="30").pack()
space=Label(text="").pack()

# Function Exit, Button Exit, to Exit the program
def exit():
    main_screen.destroy()

Button(text="Quit", command=exit, width=20,bg='blue',fg='white').pack()

main_screen.mainloop() # start the GUI
