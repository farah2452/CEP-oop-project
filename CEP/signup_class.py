from tkinter import *
from PIL import Image, ImageTk


class Signup:
    
    def customer_signup(self, master=None, image=None, relief=SUNKEN, entry_bg = "#F5F5F5", label_font = "Times 16", bg = "#9C27B0", place_x=0, place_y=0):  
        
        # entry_bg = "#F5F5F5"
        # label_font = "Times 16"
        # bg = "#9C27B0"
        # self.root = Tk()
        # self.root.title("Customer Login")
        # self.root.geometry("990x630+210+15")
        # self.root.maxsize(width=990, height=670)
        # self.root.minsize(width=990, height=670)
        # self.root.config(background=bg)

        # Form Frame with fields
        self.form_frame = Frame(master, relief=relief, bd=5)
        
        if image != None:
            self.image = ImageTk.PhotoImage(Image.open(image)).resize((360, 600))
            self.image_label = Label(self.form_frame, image=self.image).pack(pady=10)

        self.signup_form = LabelFrame(self.form_frame, text="SIGN UP", font=("Times", "22", "bold"))

        self.subheader_lab = Label(self.signup_form,
                                   text="Please fill in this form to create an account!",
                                   font="Times 15").pack(side=TOP, anchor="w", pady=10, padx=5)
        
        self.form_entries  = Frame(self.signup_form)
        
        # Entry variables
        self.fname = StringVar()
        self.lname = StringVar()
        self.username = StringVar()
        self.mail = StringVar()
        self.password = StringVar()

        # Label for the fields
        self.fields = ("First name", "Last name", "Username", "Email Address", "Password")

        for field in range(len(self.fields)):
            self.field_label = Label(self.form_entries, font=label_font, text=self.fields[field])
            self.field_label.grid(row=field, column=0, pady=15)

        # Entry for the fields
        self.entries = (self.fname, self.lname, self.username, self.mail, self.password)

        for entry in range(len(self.entries)):
            self.field_enter = Entry(self.form_entries, textvar=self.entries[entry],
                                     bg=entry_bg, width=40, relief=SOLID)
            self.field_enter.grid(row=entry, column=1, pady=3, padx=15)
            
        # Sign Up Button
        self.register_button = Button(self.form_frame, text="Sign Up", font=label_font,
                                      relief=SUNKEN, bd=3, padx=20, fg="white", bg="#1976D2").pack(side=BOTTOM, pady=10)


        # packing  widgets
        self.form_entries.pack(pady=5,padx=40)
        self.signup_form.pack(pady=10,padx=10)
        self.form_frame.place(x=place_x, y=place_y)
        

    def seller_signup(self, master=None, image=None, relief=SUNKEN, entry_bg = "#F5F5F5", label_font = "Times 16", bg = "#9C27B0", place_x=0, place_y=0):  
        
        # entry_bg = "#F5F5F5"
        # label_font = "Times 16"
        # bg = "#9C27B0"
        # self.root = Tk()
        # self.root.title("Customer Login")
        # self.root.geometry("990x630+210+15")
        # self.root.maxsize(width=990, height=670)
        # self.root.minsize(width=990, height=670)
        # self.root.config(background=bg)

        # Form Frame with fields
        self.form_frame = Frame(master, relief=relief, bd=5)
        
        if image != None:
            self.image = ImageTk.PhotoImage(Image.open(image)).resize((360,600))
            self.image_label = Label(self.form_frame, image = self.image).pack(pady = 10)

        self.signup_form = LabelFrame(self.form_frame, text="SIGN UP", font=("Times", "22", "bold"), labelanchor="n")

        self.subheader_lab = Label(self.signup_form,
                                   text="Please fill in this form to create an account!",
                                   font="Times 15").pack(side=TOP, anchor="w", pady=10, padx=5)
        
        self.form_entries  = Frame(self.signup_form)
        
        # Entry variables
        self.fname = StringVar()
        self.lname = StringVar()
        self.username = StringVar()
        self.mail = StringVar()
        self.password = StringVar()

        # Label for the fields
        self.fields = ("First name", "Last name", "Username", "Email Address", "Password")

        for field in range(len(self.fields)):
            self.field_label = Label(self.form_entries, font=label_font, text=self.fields[field])
            self.field_label.grid(row=field, column=0, pady=15)

        # Entry for the fields
        self.entries = (self.fname, self.lname, self.username, self.mail, self.password)

        for entry in range(len(self.entries)):
            self.field_enter = Entry(self.form_entries, textvar=self.entries[entry],
                                     bg=entry_bg, width=40, relief=SOLID)
            self.field_enter.grid(row=entry, column=1, pady=3, padx=15)
            
        # Sign Up Button
        self.register_button = Button(self.form_frame, text="Sign Up", font=label_font,
                                      relief=SUNKEN, bd=3, padx=20, fg="white", bg="#1976D2").pack(pady=10)

        # packing  widgets
        self.form_entries.pack(pady=5,padx=40)
        self.signup_form.pack(pady=10,padx=10)
        self.form_frame.place(x=place_x, y=place_y)


# root = Tk()
# root.geometry("500x400")
# a = Signup()

# a.customer_signup(root,place_x=200,place_y=100)

# root.mainloop()

