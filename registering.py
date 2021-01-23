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
root.geometry('800x800')
root.title("Registration Form")
registrationLabel = Label(root, text="Registration form",width=20,font=("bold", 20))
registrationLabel.place(x=150,y=53)

# Labels
id_lbl = Label(root, text="ID Number:",width=20,font=("bold", 10))
id_lbl.place(x=80,y=120)
name_lbl = Label(root, text="Name:",width=20,font=("bold", 10))
name_lbl.place(x=80,y=160)
surname_lbl = Label(root, text="Surname:",width=20,font=("bold", 10))
surname_lbl.place(x=80,y=200)
age_lbl = Label(root, text="Age:",width=20,font=("bold", 10))
age_lbl.place(x=80,y=240)
dob_lbl = Label(root, text="Date Of Birth:",width=20,font=("bold", 10))
dob_lbl.place(x=80,y=280)
gender_lbl = Label(root, text="Gender:",width=20,font=("bold", 10))
gender_lbl.place(x=80,y=320)
phoneNo_lbl = Label(root, text="PhoneNumber:",width=20,font=("bold", 10))
phoneNo_lbl.place(x=80,y=360)
email_lbl = Label(root, text="Email:",width=20,font=("bold", 10))
email_lbl.place(x=80,y=400)
username_lbl = Label(root, text="Username:",width=20,font=("bold", 10))
username_lbl.place(x=80,y=440)
password_lbl = Label(root, text="Password:",width=20,font=("bold", 10))
password_lbl.place(x=80,y=480)

# Entries
id_entry = Entry(root)
id_entry.place(x=240,y=115)
name_entry= Entry(root)
name_entry.place(x=240,y=155)
surname_entry = Entry(root)
surname_entry.place(x=240,y=195)
age_entry = Entry(root)
age_entry.place(x=240,y=235)
dob_entry = Entry(root)
dob_entry.place(x=240,y=275)
gender_entry = Entry(root)
gender_entry.place(x=240,y=315)
phone_entry = Entry(root)
phone_entry.place(x=240,y=355)
email_entry = Entry(root)
email_entry.place(x=240,y=395)
username_entry = Entry(root)
username_entry.place(x=240,y=435)
password_entry = Entry(root)
password_entry.place(x=240,y=475)

mycursor = mydb.cursor()

def register_user():
    # getting the users input
    id_number = id_entry.get()
    name = name_entry.get()
    surname = surname_entry.get()
    age = age_entry.get()
    dob=dob_entry.get()
    gender=gender_entry.get()
    phone=phone_entry.get()
    email = email_entry.get()
    user_name = username_entry.get()
    pass_word = password_entry.get()
    try:
        # inserting entered values in the database
        sql = "INSERT INTO Register VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"
        mycursor.execute(sql, [id_number, name, surname, age, dob, gender, phone, email, user_name, pass_word])
        result = mycursor.fetchone()
        mydb.commit()
        # if the data is insterted successfully Record inserted message is displayed
        messagebox.showinfo("INSERTION", "Record Inserted")
    except:
        # If not, insertion failed is displayed
        messagebox.showinfo("INSERTION", "Record Insertion failed")


insert_btn=Button(root,command=register_user, text='Insert',width=20,bg='blue',fg='white').place(x=220,y=560)


# Exit function
def exit():
    root.destroy()

btnExit=Button(root, text="Quit", command=exit, width=20,bg='blue',fg='white')
btnExit.place(x=220,y=590)
root.mainloop()

