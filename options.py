from tkinter import *

# Setting up a window
login_screen = Tk()
login_screen.title("Options")
login_screen.geometry("300x300")

# Skipping a line
Label(login_screen, text="                              OPTIONS!!!                            ", bg="grey").pack()
Label(login_screen, text="").pack()

# Press button Register to go to the registration window
def visitor():
    import registering
    registering.registration()

# Set register button
Button(login_screen,command=visitor, text="Visitor Register", width=20, height=2, bg="blue",fg='white').pack()
Label(login_screen, text="").pack()
def user():
    import loggingin
    loggingin.login()

# Set register button
Button(login_screen,command=user, text="User Login", width=15, height=2, bg="blue",fg='white').pack()
Label(login_screen, text="").pack()
def admin():
    import main

# Set register button
Button(login_screen,command=admin, text="Admin", width=10, height=2, bg="blue",fg='white').pack()
Label(login_screen, text="").pack()
def exit():
    login_screen.destroy()

Button(text="Quit", command=exit, width=5, height=1,bg='blue',fg='white').pack()

login_screen.mainloop() # start the GUI
