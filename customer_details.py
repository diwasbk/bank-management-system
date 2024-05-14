from tkinter import *
root = Tk()
import sqlite3
root.title("Customer Details")

#Labels Bar
line_label = Label(root, text="__________________________________________________________________________________________________________________________________________________________________________________________", font=("Arial", 16, "bold"),fg="green")
line_label.place(y=25)

account_number_label = Label(root, text="Acount Number ", font=("Arial", 12, "bold"),fg="blue")
account_number_label.grid(row=1, column=1,padx=40,pady=20)

name_label = Label(root, text="Name  ", font=("Arial", 12, "bold"),fg="blue")
name_label.grid(row=1, column=2,padx=70,pady=20)

gender_label = Label(root, text="Gender ", font=("Arial", 12, "bold"),fg="blue")
gender_label.grid(row=1, column=3,padx=10,pady=20)

dob_label = Label(root, text="DOB  ", font=("Arial", 12, "bold"),fg="blue")
dob_label.grid(row=1, column=4,padx=40,pady=20)

email_label = Label(root, text="Email ", font=("Arial", 12, "bold"),fg="blue")
email_label.grid(row=1, column=5,padx=60,pady=20)

phone_number_label = Label(root, text="PhoneNumber", font=("Arial", 12, "bold"),fg="blue")
phone_number_label.grid(row=1, column=6,padx=30,pady=20)

address_label = Label(root, text="Address", font=("Arial", 12, "bold"),fg="blue")
address_label.grid(row=1, column=7,padx=50,pady=20)

current_balance_label = Label(root, text="NPR", font=("Arial", 12, "bold"),fg="blue")
current_balance_label.grid(row=1, column=8,padx=40,pady=20)

#Establishing database
conn = sqlite3.connect('Bank Management System.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM accounts")
details = cursor.fetchall()
num=2
for i in details:
    account_number_label=Label(root, text=i[0],font=("Arial", 10, "bold"))
    account_number_label.grid(row=num,column=1,padx=2,pady=5)

    name_label=Label(root, text=i[1],font=("Arial", 10, "bold"))
    name_label.grid(row=num,column=2,padx=2,pady=5)

    gender_label=Label(root, text=i[2],font=("Arial", 10, "bold"))
    gender_label.grid(row=num,column=3,padx=2,pady=5)

    dob_label=Label(root, text=i[3],font=("Arial", 10, "bold"))
    dob_label.grid(row=num,column=4,padx=2,pady=5)

    email_label=Label(root, text=i[4],font=("Arial", 10, "bold"))
    email_label.grid(row=num,column=5,padx=2,pady=5)

    phone_number_label=Label(root, text=i[5],font=("Arial", 10, "bold"))
    phone_number_label.grid(row=num,column=6,padx=2,pady=5)

    address_label=Label(root, text=i[6],font=("Arial", 10, "bold")) 
    address_label.grid(row=num,column=7,padx=2,pady=5)

    current_balance_label = Label(root, text=i[7], font=("Arial", 12, "bold"),fg="green")
    current_balance_label.grid(row=num, column=8,padx=2,pady=5)

    num=num+1

conn.commit()
conn.close()

root.mainloop()
