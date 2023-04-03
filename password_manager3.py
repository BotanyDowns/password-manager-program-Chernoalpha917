from tkinter import *
import os

root = Tk()
root.title("Login")
root.geometry("700x700")

unpw = {}
with open("password2.txt") as file:
    password_true = file.readline().strip()

def frames1():
    global frame1
    frame1 = Frame(root)
    frame1.grid(row=0, column=0, sticky="nsew")

    #placing objects in frame one
    lblPass = Label(frame1, text="New User please Enter Password")
    lblPass.grid(row=0, column=0)

    entryPass = Entry(frame1, show="•")
    entryPass.grid(row=0, column=1)

    btnLogin = Button(frame1, text="Log In", command=lambda: set_password(entryPass.get()))
    btnLogin.grid(row=2, column=1)

    lblPass = Label(frame1, text="You will need to remember this password \n as this app will ask you for it next time you sign in")
    lblPass.grid(row=3, column=0)

def set_password(password):
    with open("password2.txt", "w") as file:
        file.write(password)

    global password_true
    password_true = password 
    frames2()

def frames2():
    global frame2
    frame2 = Frame(root)
    frame2.grid(row=0, column=0, sticky="nsew")

    lblPass = Label(frame2, text="Enter App Password")
    lblPass.grid(row=1, column=0)

    entryPass = Entry(frame2, show="•")
    entryPass.grid(row=1, column=1)

    btnLogin = Button(frame2, text="Log In", command=lambda: check_password(entryPass.get(), error_label))
    btnLogin.grid(row=2, column=1)

    error_label = Label(frame2, fg="red")
    error_label.grid(row=3, column=1, pady=10)

def check_password(password, error_label):
    global frame3
    if password == password_true:
        frame3 = Frame(root, bg="red")
        frame3.grid(row=0, column=0, sticky="NSEW")

        lblAccount = Label(frame3, text="AccountName")
        lblAccount.grid(row=0, column=0)

        entryAccount = Entry(frame3)
        entryAccount.grid(row=0, column=1)

        lblPass = Label(frame3, text="Password")
        lblPass.grid(row=1, column=0)

        entryPass = Entry(frame3, show="*")
        entryPass.grid(row=1, column=1)
        
        def clear_text():
            entryAccount.delete(0, END)
            entryPass.delete(0, END)
        
        btnEnter = Button(frame3, text="Enter", command=lambda: (accounts(entryAccount.get(), entryPass.get()), clear_text()))
        btnEnter.grid(row=2, column=1)

        btnView = Button(frame3, text="View Saved Passwords", command=view_passwords)
        btnView.grid(row=3, column=1)

        btnClearAll = Button(frame3, text="Clear All Passwords", command=clear_all_passwords)
        btnClearAll.grid(row=4, column=1)

        btnClearAppPassword = Button(frame3, text="Clear App Password", command=clear_app_password)
        btnClearAppPassword.grid(row=5, column=1)

        btnView = Button(frame3, text="View Saved Passwords", command=view_passwords)
        btnView.grid(row=3, column=1)

    else:
        error_label.config(text="Password is INCORRECT! Please try again")

#displays passwords
def view_passwords():
    global frame3
    frame3 = Frame(root, bg="red")
    frame3.grid(row=0, column=0, sticky="NSEW")

    with open("PMResults2.txt", "r") as f:
        data = f.read()

    text_box = Text(frame3)
    text_box.insert(INSERT, data)
    text_box.grid(row=0, column=0)

    btnClose = Button(frame3, text="Close", command=frame3.destroy)
    btnClose.grid(row=1, column=0)

#shows results
def clear_all_passwords():
    global unpw
    unpw = {}
    with open("PMResults2.txt", "w") as file:
        file.write("")

def clear_app_password():
    global password_true
    password_true = "!placeholder_password!"
    with open("password2.txt", "w") as file:
        file.write(password_true)
    frame3.destroy()
    frames1()

def accounts(entryAccount, entryPass):
    unpw[entryAccount] = entryPass
    with open("PMResults2.txt", "a") as file:
        file.write(f"{entryAccount}: {entryPass}\n")
    print(entryAccount, entryPass)



if password_true == "!placeholder_password!":
    frames1()
else:
    frames2()

root.mainloop()
