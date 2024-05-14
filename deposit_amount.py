from tkinter import *
root = Tk()
root.title("Deposit Amount")
root.geometry("650x350")
root.resizable(0, 0)
import sqlite3
from tkinter import messagebox

def clear():
    account_number_entry.delete(0, END)
    amount_entry.delete(0, END)

def deposit():
    conn = sqlite3.connect('Bank Management System.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Balance FROM accounts WHERE AC_No=?", (account_number_entry.get(),))
    result = cursor.fetchone()

    amount = amount_entry.get()
    
    if amount != "":
        if amount.isdigit() and float(amount) >= 0:
            if result:
                current_balance = result[0]
                new_balance = current_balance + float(amount)
                cursor.execute("UPDATE accounts SET Balance=? WHERE AC_No=?", (new_balance, account_number_entry.get()))
                conn.commit()

                messagebox.showinfo("Deposited Successfully", f"NPR {float(amount)} has been deposited successfully!")
            else:
                messagebox.showerror("Error", "Account not found")
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid non-negative numeric amount")
    else:
        messagebox.showinfo("Invalid", "All the fields are mandatory to fill")

    conn.close()

heading_label = Label(root, text="Deposit Amount", font=("Arial", 20, "bold"))
heading_label.place(x=250, y=20)

account_number_label = Label(root, text="Account number: ", font=("Arial ", 12, "bold"))
account_number_label.place(x=100, y=120)

amount_label = Label(root, text="Amount: ", font=("Arial ", 12, "bold"))
amount_label.place(x=100, y=180)

account_number_entry = Entry(root, width=30)
account_number_entry.place(x=250, y=120)

amount_entry = Entry(root, width=30)
amount_entry.place(x=250, y=180)

deposit_btn = Button(root, text="Deposit", font=("Arial Bold", 12), fg="white", bg="green", width=10, cursor="hand2", command=deposit)
deposit_btn.place(x=300, y=240)

clear_btn = Button(root, text="Clear", font=("Arial Bold", 12), fg="white", bg="red", width=10, cursor="hand2", command=clear)
clear_btn.place(x=450, y=240)

root.mainloop()