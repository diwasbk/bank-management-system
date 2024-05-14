from tkinter import *
root=Tk()
root.title("Check Balance")
root.geometry("700x400")
root.resizable(0,0)
import sqlite3
from tkinter import messagebox

def clear():
    account_number_entry.delete(0, END)
    name_label.destroy()
    amount_label.destroy()

def check():
    global name_label
    global amount_label
    conn = sqlite3.connect('Bank Management System.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Balance FROM accounts WHERE AC_No=?", (account_number_entry.get(),))
    result1 = cursor.fetchone()
    cursor.execute("SELECT Name FROM accounts WHERE AC_No=?", (account_number_entry.get(),))
    result2 = cursor.fetchone()

    if result1 and result2:
        current_balance = result1[0]
        name=result2[0]

        name_label=Label(root, text=f"Name: {name} ",font=("Arial ",12,"bold"),fg="green")
        name_label.place(x=100,y=160)

        amount_label=Label(root, text=f"Current Balance: NPR {current_balance} ",font=("Arial ",12,"bold"),fg="green")
        amount_label.place(x=100,y=200)
    else:
       messagebox.showerror("Error", "Account not found")

heading_label=Label(root, text="Check Balance", font=("Arial", 20, "bold"))
heading_label.place(x=250, y=20)

account_number_label=Label(root, text="Account Number:", font=("Arial", 12,"bold"))
account_number_label.place(x=100, y=120)

account_number_entry=Entry(root, font=("Arial", 12))
account_number_entry.place(x=250, y=120)

check_btn=Button(root, text="Check", font=("Arial Bold", 12),fg="white",bg="green",width=10,cursor="hand2",command=check)
check_btn.place(x=300, y=300)

clear_btn=Button(root, text="Clear", font=("Arial Bold", 12),fg="white",bg="red",width=10,cursor="hand2",command=clear)
clear_btn.place(x=450, y=300)


root.mainloop()
