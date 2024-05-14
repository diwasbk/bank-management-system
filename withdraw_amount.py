from tkinter import*
root=Tk()
root.title("Withdraw Amount")
root.geometry("650x350")
root.resizable(0,0)
import sqlite3
from tkinter import messagebox

def clear():
    account_number_entry.delete(0, END)

def withdraw():
    conn = sqlite3.connect('Bank Management System.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Balance FROM accounts WHERE AC_No=?", (account_number_entry.get(),))
    result = cursor.fetchone()
    if amount_entry.get()!="":
        if result:
            current_balance = result[0]
            if current_balance>=float(amount_entry.get()):
                new_balance = current_balance - float(amount_entry.get())
                cursor.execute("UPDATE accounts SET Balance=? WHERE AC_No=?", (new_balance, account_number_entry.get()))
                conn.commit()
                messagebox.showinfo("Withdrawn Successfully", f"NPR {(float(amount_entry.get()))} has been withdrawn successfully!")   
            else:
                 messagebox.showerror("Insufficient Amount", "Sorry! This account doesn't have sufficient amount of balance.")

        else:
             messagebox.showerror("Error", "Account not found")
    else:
        messagebox.showinfo("Invalid","All the fields are mandatory to fill")
    conn.close()

heading_label=Label(root, text="Withdraw Amount",font=("Arial", 20,"bold"))
heading_label.place(x=250, y=20)

account_number_label=Label(root, text="Account number : ",font=("Arial ",12,"bold"))
account_number_label.place(x=100,y=120)

amount_label=Label(root, text="Amount : ",font=("Arial ",12,"bold"))
amount_label.place(x=100,y=180)

account_number_entry=Entry(root,width=30)
account_number_entry.place(x=250,y=120)

amount_entry=Entry(root,width=30)
amount_entry.place(x=250,y=180)

withdraw_btn=Button(root, text="Withdraw", font=("Arial Bold",12),fg="white",bg="green",width=10,cursor="hand2",command=withdraw)
withdraw_btn.place(x=300, y=240)

clear_btn=Button(root, text="Clear", font=("Arial Bold", 12),fg="white",bg="red",width=10,cursor="hand2",command=clear)
clear_btn.place(x=450, y=240)

root.mainloop()
