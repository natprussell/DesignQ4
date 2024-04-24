from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("250x200")
root.title("Login")

email_label = ttk.Label(root, text="Email:")
email_label.pack()
email_entry = ttk.Entry(root)
email_entry.pack()

password_label = ttk.Label(root, text="Password:")
password_label.pack()
password_entry = ttk.Entry(root, show="*")
password_entry.pack()

signin_button = ttk.Button(root, text="Sign In")
signin_button.pack()

status_label = ttk.Label(root, text="")
status_label.pack()

root.mainloop()