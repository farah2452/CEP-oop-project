from tkinter import *
from PIL import Image, ImageTk


class Signup:
    def customer_signup(self):
        entry_bg = "#F5F5F5"
        label_font = "Times 16"
        bg = "#9C27B0"
        self.root = Tk()
        self.root.title("Customer Login")
        self.root.geometry("990x630+210+15")
        self.root.maxsize(width=990, height=670)
        self.root.minsize(width=990, height=670)
        self.root.config(background=bg)

        # Form Frame with fields
        self.form_frame = Frame(self.root, relief=SUNKEN, bd=5, height=600)

        self.header_lab = Label(self.form_frame, text="SIGN UP", font=("Times", "22", "bold"))

        self.subheader_lab = Label(self.form_frame,
                                   text="Please fill in this form to create an account!",
                                   font="Times 15")

        # Entry variables
        self.fname = StringVar()
        self.lname = StringVar()
        self.username = StringVar()
        self.mail = StringVar()
        self.password = StringVar()

        # Label for the fields
        self.fields = ("First name", "Last name", "Username", "Email Address", "Password")

        for field in range(len(self.fields)):
            self.field_label = Label(self.form_frame, font=label_font, text=self.fields[field])
            self.field_label.grid(row=2 + field, column=0, pady=20)

        # Entry for the fields
        self.entries = (self.fname, self.lname, self.username, self.mail, self.password)

        for entry in range(len(self.entries)):
            self.field_enter = Entry(self.form_frame, textvar=self.entries[entry],
                                     bg=entry_bg, width=40, relief=SOLID)
            self.field_enter.grid(row=2 + entry, column=1, pady=20, padx=30)

        # Sign Up Button
        self.register_button = Button(self.form_frame, text="Sign Up", font=label_font,
                                      relief=SUNKEN, bd=3, padx=30, fg="white", bg="#1976D2")

        # packing  widgets
        self.form_frame.place(x=154, y=50, anchor=NW)
        self.header_lab.grid(row=0, column=0, pady=5)
        self.subheader_lab.grid(row=1, column=0, padx=5, pady=7)
        self.register_button.grid(row=7, column=1, pady=30, columnspan=2)

        self.root.mainloop()


r = Signup()
r.customer_signup()


