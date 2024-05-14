from tkinter import *
from tkinter import messagebox


def submit():
    username = user.get()
    password = passw.get()

    if username == "JASHAN" and password == "123":
        messagebox.showinfo("Login Successful", "Welcome Jashan!")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")


root = Tk()
root.title("Login Page")

frame = Frame(root)
frame.pack()

user = StringVar()
passw = StringVar()

label1 = Label(frame, text='Username')
label1.grid(row=0, column=0)
entry1 = Entry(frame, textvariable=user)
entry1.grid(row=0, column=1)

label2 = Label(frame, text='Password')
label2.grid(row=1, column=0)
entry2 = Entry(frame, textvariable=passw, show='*')
entry2.grid(row=1, column=1)

submit_button = Button(frame, text='Submit', command=submit)
submit_button.grid(row=2, column=1)

root.mainloop()


















