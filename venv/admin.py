from tkinter import *
import mysql.connector
from tkinter import messagebox

admin_page = Tk()   # create a GUI window
admin_page.geometry("1050x600") # set the configuration of GUI window
admin_page.title("Admin Page") # set the title of GUI window
def makeAdmin():
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="lifechoices1",
      password="@Lifechoices1234",
        database="lifechoicesonline", auth_plugin='mysql_native_password'
    )

    # Label with the name of the page
    Label(admin_page, text="Welcome to the Admin Page",font=("Courier",25)).place(x=300,y=50)
    # Takes you to the add users page
    def addUser():
        import registering
        registering.register_user()

    btnAdd = Button(admin_page,command=addUser, text="Add New", bg="blue",width=15).place(x=0,y=250)
    # Deletes the User
    def deleteUser():

        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="lifechoices1",
          password="@Lifechoices1234",
            database="lifechoicesonline", auth_plugin='mysql_native_password'
        )
        mycursor=mydb.cursor()
        mycursor.execute("DELETE FROM Register WHERE id_number=%s", id_number.get())

        mycursor.commit()
        messagebox.showinfo("DELETE USER","Data successfully Deleted")
    btnDelete = Button(admin_page,command=deleteUser, text="Delete", bg="blue",width=15).place(x=150,y=250)
    # Sign's out time
    def signUser_out():
        timeout = datetime.now()
        y = timeout.strftime("%H:%M:%S")
        z = userent.get()
        infoTime = z, x, y
        timeComm = "INSERT INTO SignOut(id,Username,Code,DateAndTime) VALUES(%s, %s, %s,curtime()"

        mycursor.execute(timeComm, infoTime)
        mydb.commit()
        messagebox.showinfo('Signout Message', 'Signed out!')
        admin_page.destroy()

    btnSignOut = Button(admin_page,command=signUser_out,text="Display SignOut", bg="blue",width=15).place(x=300,y=250)
    # Takes you to the page which adds an admin
    def addAdmin():
        import addAdmin

    btnAddAmin = Button(admin_page,command=addAdmin, text="Add Admin", bg="blue",width=15).place(x=450,y=250)
    # Update function which adds the information to the User Table and the time is also addes to the users table
    def update():
        username=user_name.get()
        code=code.get()
        id = id_no.get()

        sql = "UPDATE User SET Category='%s',DateAndTime='%s', Username = '%s', Code = '%s' WHERE id='%s';"



        mycursor.execute(sql, [(id),(username),(code)])

        mydb.commit()



    btnSigin = Button(admin_page,command=update, text="SignIn", bg="blue",width=15).place(x=600,y=250)
    # Exit Function
    def exit():
        exit = messagebox.askyesno("Admin Exit", "Are you sure you want to exit?")
        if exit > 0:
            admin_page.destroy()
            return

    btnExit = Button(admin_page,command=exit, text="Exit", bg="blue",width=15).place(x=750,y=250)
    # Displaying all names in the list box
    def Display():

        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="lifechoices1",
          password="@Lifechoices1234",
            database="lifechoicesonline", auth_plugin='mysql_native_password'
        )
        mycursor= mydb.cursor()
        mycursor.execute("SELECT * FROM Register")
        for i in listOfUsers:
            listBox.insert(END,i)

        mydb.commit()


    mycursor= mydb.cursor()
    listBox = Listbox(admin_page, width=300)
    listBox.place(x=0, y=300)

    listOfUsers = [[mycursor.execute("SELECT * FROM Register")]]


    btnReset=Button(command=Display, text="Display/Reset", bg="blue",width=15).place(x=400,y=500)

    # Clearing the list box
    def clear_all():
        listBox.delete(0, END)


    btnClear=Button(command=clear_all, text="Clear", bg="blue",width=15).place(x=900,y=250)
    # CREAING A HOT KEY (PRESS Cntrl+a)

    # Labels
    lblUsername=Label(admin_page,text="Username: ").place(x=80,y=120)
    lblCode=Label(admin_page,text="Code: ").place(x=80,y=160)
    lbl_id = Label(admin_page,text="ID Number: ").place(x=80,y=200)
    # Entries
    user_name=Entry(admin_page).place(x=240,y=115)
    code=Entry(admin_page).place(x=240,y=155)
    id= Entry(admin_page).place(x=240,y=195)



def key():
    MakeAdmin()
admin_page.bind("<Control-a>", lambda x: key())
makeAdmin()
admin_page.mainloop()
