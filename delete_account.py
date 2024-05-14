from tkinter import *
root=Tk()
root.title("Delete Account")
root.geometry("700x400")
root.resizable(0,0)

import sqlite3
from tkinter import messagebox

def delete():
    conn = sqlite3.connect('Bank Management System.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE AC_No=?", (account_number_entry.get(),))
    account = cursor.fetchone()
    if account:
        cursor.execute("DELETE FROM accounts WHERE AC_No=?", (account_number_entry.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Successfully Deleted", f"AC No: {account_number_entry.get()} has been deleted successfully")
        import customer_details
    else:
        messagebox.showerror("Account Not Found", f"The account number '{account_number_entry.get()}' does not exist.")

def clear():
    account_number_entry.delete(0, END)


heading_lbl=Label(root, text="Delete Account", font=("Arial", 20, "bold"))
heading_lbl.place(x=250, y=20)

account_number_label=Label(root, text="Account Number:", font=("Arial", 12,"bold"))
account_number_label.place(x=100, y=120)

account_number_entry=Entry(root, font=("Arial", 12))
account_number_entry.place(x=250, y=120)

delete_btn=Button(root, text="Delete", font=("Arial Bold", 12),fg="white",bg="red",width=10,cursor="hand2",command=delete)
delete_btn.place(x=300, y=300)

clear_btn=Button(root, text="Clear", font=("Arial Bold", 12),fg="white",bg="black",width=10,cursor="hand2",command=clear)
clear_btn.place(x=450, y=300)

root.mainloop()