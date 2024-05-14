from tkinter import *
root=Tk()
root.title("Create New Account")
root.geometry("750x520")
root.resizable(0,0)

import sqlite3
from tkinter import messagebox


def generate_ac_no():
    import random
    import string
    random_number = ''.join(str(random.randint(0, 9))for i in range(11))
    alphabet = random.choice(string.ascii_uppercase)
    account_number = "00"+(random_number) + ""+alphabet
    account_number_entry.delete(0, END)
    account_number_entry.insert(0,account_number)

# Creating Database
conn = sqlite3.connect('Bank Management System.db')
cursor = conn.cursor()
cursor.execute('''
          CREATE TABLE IF NOT EXISTS accounts (
              AC_No TEXT PRIMARY KEY,
              Name TEXT,
              Gender TEXT,
              DOB TEXT,
              Email TEXT,
              Phone_Number TEXT,
              Address TEXT,
              Balance REAL DEFAULT 0.0
          )
          ''')
conn.commit()
conn.close()


def submit():
    if account_number_entry.get() == "" or name_entry.get() == "" or dob_entry.get() == "" or email_entry.get() == "" or phone_number_entry.get() =="" or address_entry.get()=="": 
        messagebox.showerror("Incomplete Information", "Please complete all the fields")
    elif not email_entry.get().endswith("@gmail.com"):
        messagebox.showerror("Error", "Invalid gmail account")
    elif len(phone_number_entry.get()) != 10:
        messagebox.showerror("Error", "Invalid phone number")
    else:
        conn = sqlite3.connect('Bank Management System.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
               (account_number_entry.get(),
                name_entry.get().upper(),
                gender.get(),
                dob_entry.get().upper(),
                email_entry.get().lower(),
                phone_number_entry.get(),
                address_entry.get().upper(),
                0.0
               )
              )


        conn.commit()
        conn.close()
        messagebox.showinfo("Account Created Successfully", f"AC No: {account_number_entry.get()} has been created successfully")


def clear():
    account_number_entry.delete(0, END)
    name_entry.delete(0, END)
    dob_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    address_entry.delete(0, END)

#Labels

heading_label=Label(root, text="Create New Account",font=("Arial", 20, "bold"))
heading_label.place(x=250, y=20)

account_number_label=Label(root, text="Account Number : ",font=("Arial ",12,"bold"))
account_number_label.place(x=100,y=120)

name_label=Label(root, text="Name : ",font=("Arial ",12,"bold"))
name_label.place(x=100,y=160)

gender_label=Label(root, text="Select Gender : ",font=("Arial ",12,"bold"))
gender_label.place(x=100,y=200)

gender = StringVar()
radio1 = Radiobutton(root, text="Male", font=("Arial ", 10), variable=gender, value="Male")
radio1.place(x=250, y=200)
radio2 = Radiobutton(root, text="Female", font=("Arial ", 10), variable=gender, value="Female")
radio2.place(x=320, y=200)



dob_label=Label(root, text="DOB : ",font=("Arial ",12,"bold"))
dob_label.place(x=100,y=240)

email_label=Label(root, text="Email : ",font=("Arial ",12,"bold"))
email_label.place(x=100,y=280)

phone_number_label=Label(root, text="Phone Number : ",font=("Arial ",12,"bold"))
phone_number_label.place(x=100,y=320)

address_label=Label(root, text="Address : ",font=("Arial ",12,"bold"))
address_label.place(x=100,y=360)

#Entry Boxes

account_number_entry=Entry(root,width=30)
account_number_entry.place(x=250,y=120)

name_entry=Entry(root,width=30)
name_entry.place(x=250,y=160)

dob_entry=Entry(root,width=30)
dob_entry.place(x=250,y=240)

email_entry=Entry(root,width=30)
email_entry.place(x=250,y=280)

phone_number_entry=Entry(root,width=30)
phone_number_entry.place(x=250,y=320)

address_entry=Entry(root,width=30)
address_entry.place(x=250,y=360)

#Buttons
generate_ac_no_btn=Button(root, text=("Generate AC No"), font=("Arial Bold", 12), fg="white", bg="#00BFFF", width=15, cursor="hand2", command=generate_ac_no)
generate_ac_no_btn.place(x=100, y=420)

submit_btn=Button(root, text=("Submit"), font=("Arial Bold", 12),fg="white",bg="green",width=10,cursor="hand2",command=submit)
submit_btn.place(x=300,y=420)

clear_btn=Button(root, text=("Clear"), font=("Arial Bold", 12),fg="white",bg="red",width=10,cursor="hand2",command=clear)
clear_btn.place(x=450,y=420)

root.mainloop()
